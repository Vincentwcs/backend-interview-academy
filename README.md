# Backend Interview Academy

中文后端工程师面试知识学习站点，当前为 V1.0 静态原型。

## 学习模块

- Java 基础与集合
- 并发编程与线程安全
- JVM 与性能调优
- Spring / Spring Boot
- MySQL / 数据库
- Redis / Kafka / 分布式系统
- 金融清算与架构实战

当前包含 41 个知识点，支持关键词搜索、模块筛选、掌握度自评、复习标记和浏览器本地进度保存。

## 本地预览

直接使用浏览器打开仓库根目录的 `index.html`，无需构建步骤或后端服务。

## GitHub Pages 部署

仓库已包含 GitHub Actions 工作流：`.github/workflows/deploy.yml`。

在 GitHub 仓库 **Settings → Pages** 中，将 **Build and deployment → Source** 设置为 **GitHub Actions**。每次向 `main` 推送提交，工作流会自动构建并发布站点。

默认站点地址：

`https://vincentwcs.github.io/backend-interview-academy/`

## 当前版本边界

- 学习进度仅保存在当前浏览器的 `localStorage`，不会跨设备同步。
- 当前是静态知识学习原型，不包含完整 CourseCoach 课程生成、自动评分、掌握度算法或云端复习队列。
- 后续可以在此基础上逐步引入结构化课程数据、作业批改与复习调度。

## 隐私说明

本仓库只包含通用技术学习内容和静态网站代码。请勿提交个人身份信息、薪资、家庭信息、健康信息、公司内部资料、真实交易数据或任何生产环境敏感信息。
