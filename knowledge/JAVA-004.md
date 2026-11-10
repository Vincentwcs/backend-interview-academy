# Java 泛型与类型擦除

> **知识点 ID：** `JAVA-004`  
> **模块：** Java 语言与基础  
> **优先级：** P0（核心）  
> **深度：** D1 概念 + D2 机制 + D3 应用  
> **状态：** 初稿，待交叉审校  
> **适用版本：** Java 8+；涉及运行时泛型信息时特别说明

## 1. 为什么要学习泛型

泛型主要解决两个问题：

1. **编译期类型约束：** 把类型错误尽量提前到编译阶段发现，而不是等到运行时才发生 `ClassCastException`。
2. **减少重复代码：** 同一套类或方法逻辑可以适用于多种类型，同时保留类型检查能力。

例如，未使用泛型的集合通常只能以 `Object` 接收元素，取出时需要强制转换；使用泛型后，编译器可以检查添加和读取的类型是否匹配。

## 2. 学习目标

完成本节后，应当能够：

- 区分泛型类、泛型接口和泛型方法。
- 解释类型擦除，以及它对运行时类型信息、重载和数组的影响。
- 区分泛型不变、上界通配符和下界通配符。
- 正确使用 PECS 原则判断 `? extends T` 与 `? super T`。
- 解释原始类型、桥接方法、可具体化类型和堆污染的基本边界。
- 阅读泛型代码并判断能否编译、运行结果及潜在风险。

## 3. 核心概念

### 3.1 泛型类与泛型方法

泛型类在类名后声明类型参数：

```java
public class Box<T> {
    private T value;

    public void set(T value) {
        this.value = value;
    }

    public T get() {
        return value;
    }
}
```

使用时指定类型实参：

```java
Box<String> box = new Box<>();
box.set("支付成功");
String value = box.get();
```

泛型方法则在返回类型前独立声明类型参数。它不要求所在类本身是泛型类：

```java
public static <T> T first(T[] values) {
    return values.length == 0 ? null : values[0];
}
```

注意：泛型方法的类型参数由方法声明，和类上的类型参数不是同一个概念；编译器通常可以根据实参进行类型推断。

### 3.2 类型参数边界

不设边界的类型参数默认可以接受任意引用类型：

```java
class Box<T> { }
```

上界限制类型参数必须是某个类型或其子类型：

```java
class NumberBox<T extends Number> {
    private T value;
}
```

多个边界使用 `&`，类边界（如果有）必须放在最前面：

```java
<T extends Number & Comparable<T>>
```

上界的意义不仅是限制传入类型，也允许在泛型实现中调用边界声明的成员。

### 3.3 泛型是不变的

即使 `Integer` 是 `Number` 的子类，`List<Integer>` 也不是 `List<Number>` 的子类。

```java
List<Integer> integers = new ArrayList<>();
// List<Number> numbers = integers; // 编译错误
```

原因是：如果允许上述赋值，后续代码就可能向 `numbers` 添加一个 `Double`，从而破坏原本 `List<Integer>` 的类型约束。

**关键结论：** Java 泛型默认是不变的。不能从类型实参的继承关系，直接推导出两个参数化类型之间的继承关系。

## 4. 通配符与 PECS

通配符表达的是“某个未知类型”，不是一个可以随意替换的类型变量。

### 4.1 上界通配符：`? extends T`

`List<? extends Number>` 表示：这是一个元素类型为某种未知类型的列表，而该未知类型是 `Number` 或其子类型。

```java
List<? extends Number> source = new ArrayList<Integer>();
Number number = source.get(0);

// source.add(1);       // 编译错误
// source.add(1.5);     // 编译错误
source.add(null);       // 可以添加 null（除非具体实现另有限制）
```

为什么不能添加一个 `Integer`？因为实际列表也可能是 `List<Double>`。编译器不知道未知类型究竟是哪一种，因此不能允许添加任意一种 `Number`。

读取时可以安全地按 `Number` 接收，因为无论未知类型是 `Integer`、`Double` 还是其他 `Number` 子类，都可以向上转型为 `Number`。

### 4.2 下界通配符：`? super T`

`List<? super Integer>` 表示：元素类型是 `Integer` 或 `Integer` 的某个父类型，例如 `Integer`、`Number` 或 `Object`。

```java
List<? super Integer> target = new ArrayList<Number>();
target.add(1);
target.add(2);

Object value = target.get(0);
```

添加 `Integer` 是安全的，因为无论实际列表是 `List<Integer>`、`List<Number>` 还是 `List<Object>`，都能接收一个 `Integer`。

读取时通常只能可靠地按 `Object` 接收，因为编译器无法确定列表实际元素类型究竟是 `Integer` 还是它的父类型。

### 4.3 PECS 原则

PECS 是帮助选择通配符方向的经验规则：

- **Producer Extends：** 如果参数主要向当前代码提供数据，倾向使用 `? extends T`。
- **Consumer Super：** 如果参数主要接收当前代码写入的数据，倾向使用 `? super T`。

例如，复制元素的方法：

```java
public static <T> void copy(
        List<? super T> destination,
        List<? extends T> source) {
    for (T item : source) {
        destination.add(item);
    }
}
```

这里源列表负责“生产”元素，因此使用 `extends`；目标列表负责“消费”元素，因此使用 `super`。

PECS 是 API 设计的实用规则，不是说一个集合绝对不能同时读写。真正的判断依据是：编译器能否证明读写操作对未知类型安全。

## 5. 类型擦除：编译器做了什么

Java 泛型主要通过编译期类型检查实现。编译器编译泛型代码时，会进行类型检查，并按规则擦除类型参数：

- 无界类型参数通常擦除为 `Object`。
- 有界类型参数擦除为其最左侧边界类型。
- 必要时插入类型转换。
- 为维持多态关系，必要时生成桥接方法。

例如：

```java
class Box<T> {
    private T value;
    public void set(T value) { this.value = value; }
    public T get() { return value; }
}
```

概念上，擦除后接近：

```java
class Box {
    private Object value;
    public void set(Object value) { this.value = value; }
    public Object get() { return value; }
}
```

这只是帮助理解的示意，不是编译器输出的逐字源码。实际字节码还包含泛型签名等元数据，供反射等机制在一定条件下读取。

### 5.1 类型擦除不等于泛型信息全部消失

需要区分两件事：

- **运行时对象的实际类型：** 例如对象本身仍然是某个具体类的实例。
- **参数化类型实参：** 普通对象通常不会在运行时携带可直接用于判断的完整泛型实参信息。

例如，不能写：

```java
// if (value instanceof List<String>) { } // 通常不允许
if (value instanceof List<?>) {
    // 可以检查它是某种 List
}
```

但字段、方法、父类声明中的部分泛型签名信息可能保留，并可通过反射 API 获取。不要把“类型擦除”理解为 class 文件中完全不存在任何泛型信息。

### 5.2 为什么不能直接创建泛型数组

以下代码不能通过编译：

```java
// T[] values = new T[10];
```

数组在运行时具有具体组件类型，并且数组会进行运行时存储检查；而泛型类型参数经过擦除后，运行时无法可靠地确定应创建哪一种具体组件类型的数组。

实践中通常优先使用集合；确实需要数组时，可以结合 `Object[]`、受控转换或 `Array.newInstance`，并把类型安全责任限制在小范围内。

### 5.3 为什么不能仅靠泛型参数重载

```java
// void process(List<String> values) {}
// void process(List<Integer> values) {}
```

这两个方法擦除后参数类型都变成 `List`，会产生相同方法签名，因此不能这样重载。

## 6. 桥接方法

考虑泛型父类和具体子类：

```java
class Parent<T> {
    public void set(T value) { }
}

class Child extends Parent<String> {
    @Override
    public void set(String value) { }
}
```

父类方法擦除后的参数类型是 `Object`，子类实际声明的方法参数类型是 `String`。为了让擦除后的方法调用仍符合覆盖关系，编译器会生成桥接方法（bridge method），概念上类似：

```java
// 编译器生成的概念示意，并非手写源码
public void set(Object value) {
    set((String) value);
}
```

桥接方法是编译器为保持多态语义生成的合成方法。通过反射可以用 `Method.isBridge()` 等方式识别。

## 7. 原始类型、堆污染与可具体化类型

### 7.1 原始类型（Raw Type）

`List` 是原始类型，`List<String>` 是参数化类型。原始类型主要为兼容早期 Java 代码而保留。

```java
List<String> names = new ArrayList<>();
List raw = names;
raw.add(100); // 编译器通常给出未经检查的警告
String name = names.get(0); // 运行时可能抛出 ClassCastException
```

原始类型绕过了泛型检查，应该尽量避免；警告不能当作无关紧要的信息。

### 7.2 堆污染（Heap Pollution）

当一个参数化类型变量实际引用了不符合其声明类型约束的对象时，就可能发生堆污染。原始类型、未经检查的转换，以及某些可变参数泛型用法都可能引入风险。

原则：尽量不使用原始类型和未经检查的转换；如果确实需要，缩小作用范围并解释安全依据。

### 7.3 可具体化类型（Reifiable Type）

可具体化类型是指运行时类型信息足以完整表示该类型的类型。普通非泛型类、原始类型、所有类型参数均为无界通配符的参数化类型（如 `List<?>`），属于常见例子。

`List<String>` 不是可具体化类型，因此不能用于普通的参数化 `instanceof` 判断，也不能创建对应的泛型数组。

## 8. 面试提纲

### 30 秒回答

Java 泛型通过编译期类型检查提升类型安全和代码复用。Java 泛型主要采用类型擦除实现：无界类型参数通常擦除为 `Object`，有界参数擦除为最左侧边界，编译器必要时插入类型转换并生成桥接方法。泛型默认不变；通配符通过 `extends` 和 `super` 表达读取与写入边界，常用 PECS 原则设计 API。

### 1 分钟回答

在 30 秒回答基础上，补充说明泛型不变的原因：如果允许 `List<Integer>` 赋值给 `List<Number>`，就可能写入 `Double`，破坏原集合的类型约束。读取生产者使用 `? extends T`，写入消费者使用 `? super T`。类型擦除还带来泛型数组创建受限、参数化类型不能直接用于普通 `instanceof`、相同擦除签名不能重载等边界。

### 3 分钟深入

按“类型安全目标 → 泛型不变 → 通配符与 PECS → 类型擦除过程 → 桥接方法 → 运行时限制与工程边界”的顺序展开。最好结合 `copy` 方法解释为什么源参数使用 `extends`、目标参数使用 `super`，再用父类 `Parent<T>` 和子类 `Child extends Parent<String>` 解释桥接方法。

## 9. 高频追问与易错边界

1. **`List<? extends Number>` 为什么不能添加 Integer？**  
   因为实际对象可能是 `List<Double>`，编译器无法证明添加 Integer 安全；读取可以按 Number 接收。
2. **`List<? super Integer>` 为什么读取只能按 Object 接收？**  
   实际类型可能是 `List<Number>` 或 `List<Object>`，元素不一定是 Integer。
3. **类型擦除后还能通过反射获取泛型吗？**  
   部分声明位置的泛型签名元数据会保留，可以通过反射读取；但不能据此认为每个运行时对象都保存了完整的泛型实参。
4. **桥接方法是程序员手写的吗？**  
   通常由编译器生成，用于维持类型擦除后的覆盖和多态语义。
5. **数组协变与泛型不变有什么区别？**  
   数组允许子类型数组赋值给父类型数组，但运行时会检查实际数组组件类型，错误写入可能触发 `ArrayStoreException`；泛型默认不变，主要在编译期阻止不安全赋值。
6. **为什么泛型方法有时不需要显式写类型参数？**  
   编译器可根据方法实参、目标类型等上下文推断类型参数。

## 10. 工程场景

假设一个后端服务需要把一批支付指令从来源集合转换后写入目标集合。API 可以声明为：

```java
public static <T> void transfer(
        Collection<? super T> destination,
        Collection<? extends T> source) {
    for (T item : source) {
        destination.add(item);
    }
}
```

这样调用方可以传入元素类型为 T 子类的来源集合，也可以传入能够接收 T 的目标集合。它降低了 API 对具体集合类型的耦合，同时保留编译期约束。

注意：泛型只能约束编译期类型关系，不能替代业务校验、幂等控制、事务一致性或并发安全设计。

## 11. 自测题

### 题 1：编译判断

下面哪一行可以编译？

```java
List<Integer> a = new ArrayList<>();
List<? extends Number> b = a;
Number n = b.get(0);
// b.add(1);
```

**答案：** 前三行可以编译；最后一行不能编译。  
**依据：** 上界通配符允许安全读取为 Number，但不能向未知子类型集合添加 Integer。

### 题 2：类型不变

`List<Integer>` 能否赋值给 `List<Number>`？为什么？

**答案：** 不能。泛型默认不变；否则可以通过父类型引用向实际的 Integer 列表写入 Double，破坏类型安全。

### 题 3：PECS

一个方法从 `List<Integer>` 读取数据，并把数据写入 `List<Number>`，参数应如何声明？

**答案：** 来源参数可声明为 `List<? extends Number>`，目标参数可声明为 `List<? super Integer>`；如果要保持元素类型之间的精确关联，也可以使用前述泛型 `copy` 方法的 `List<? extends T>` 与 `List<? super T>` 组合。

### 题 4：类型擦除

为什么不能定义两个仅参数化类型不同的重载方法：`process(List<String>)` 和 `process(List<Integer>)`？

**答案：** 两者擦除后的参数类型相同，方法签名冲突。

### 题 5：深入追问

泛型擦除后，为什么子类覆盖泛型父类方法时可能需要桥接方法？

**答案：** 父类方法擦除后的描述符与子类具体化后的方法描述符可能不同。编译器生成桥接方法，把擦除后的调用转发到子类具体方法，从而维持覆盖语义和多态行为。

## 12. 复习检查清单

- [ ] 能解释泛型类和泛型方法的区别
- [ ] 能说明泛型不变的原因
- [ ] 能独立判断 extends / super 的读写边界
- [ ] 能解释类型擦除的规则和影响
- [ ] 能说明桥接方法的产生原因
- [ ] 能识别原始类型和未经检查转换的风险
- [ ] 能用 PECS 设计一个有类型约束的集合 API

## 13. 参考资料

- Oracle Java Tutorials：Generics（泛型基础与通配符）
- Java Language Specification：Chapter 4 Types, Values, and Variables；Chapter 8 Classes；Chapter 15 Expressions
- Java SE API：`java.lang.reflect.Type`、`java.lang.reflect.ParameterizedType`、`java.lang.reflect.Method`

> 本文为课程初稿。涉及编译器实现和字节码细节时，应结合目标 JDK 的实际编译结果与官方规范核验；不要把概念示意代码误认为编译器逐字生成的源码。
