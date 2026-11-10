# Backend Interview Academy

个人后端技术面试知识学院，正在从 V1 学习进度原型演进为 V2「结构化知识库 + 主动练习 + AI 学习助教」。

## V2 建设原则

- `syllabus.md` 是课程范围、模块、知识点 ID 和优先级的唯一权威来源。
- `knowledge/` 保存独立的知识讲解材料，使用统一模板。
- `questions/` 保存结构化题目和评分依据。
- `interview-guide/` 保存面试提纲、岗位映射和回答框架。
- `index.html` 是展示与交互层，不作为知识内容的唯一存储位置。
- 学习进度属于个人数据，当前阶段保存在浏览器本地；不得提交到公开仓库。
- AI 能力后续通过服务端 API 接入，严禁把模型 API Key 写入静态前端。

## 当前网站

站点地址：<https://vincentwcs.github.io/backend-interview-academy/>

当前线上页面仍为 V1 静态原型，包含 7 个学习模块、41 个初始知识卡片、搜索筛选、掌握度自评、复习标记和浏览器本地进度保存。

## V2 文档

- [完整知识体系 syllabus](syllabus.md)
- [知识点内容模板](knowledge/TEMPLATE.md)
- [系统架构与数据边界](docs/ARCHITECTURE.md)
- [V2 实施路线图](docs/ROADMAP.md)
- [题库数据格式](questions/README.md)

## V2 课程范围

当前 syllabus 建立了 12 个一级模块：
1. Java 语言与基础
2. 集合与数据结构
3. 并发与线程安全
4. JVM 与性能
5. Spring / Spring Boot
6. MySQL / 关系型数据库
7. Redis 与缓存
8. Kafka 与消息系统
9. 分布式系统
10. 系统设计与后端工程
11. 算法、编码与工程质量
12. 金融科技、清算与支付架构

知识点按 P0（核心）、P1（重要）、P2（进阶/差异化）分级。建立目录不代表所有课程正文已经完成；内容状态会在后续逐项审核和补齐。

## 本地预览

直接使用浏览器打开仓库根目录的 `index.html`，无需构建步骤或后端服务。

## GitHub Pages 部署

仓库包含 GitHub Actions 工作流：`.github/workflows/deploy.yml`。向 `main` 推送提交后会自动发布。

## 隐私与内容边界

仓库为公开仓库，只放通用技术知识、公开规范和经过泛化的工程案例。禁止提交个人身份信息、薪资、家庭或健康信息、公司内部资料、内部系统拓扑、真实交易数据、生产代码、密钥和凭证。
