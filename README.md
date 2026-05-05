# CrewAI WebGIS UI Prototype Generator

这是一个基于 CrewAI 的 WebGIS 前端 UI 原型生成项目。

项目目标：根据用户输入的 WebGIS 项目计划书和 UI 偏好提示词，自动生成一个可运行、可浏览器查看的 Vue 3 前端原型项目。

## 项目定位

本项目不是普通文档生成器，也不是完整 WebGIS 后端系统。

它的核心能力是：

```text
项目计划书 + UI 偏好
        ↓
CrewAI 多 Agent 分析
        ↓
自动生成 Vue WebGIS 前端原型
        ↓
npm run dev 浏览器查看
```

## 技术栈

### CrewAI 生成端

- Python
- CrewAI
- UV
- 自定义 WriteProjectFileTool

### 前端原型端

- Vue 3
- TypeScript
- Vite
- Pinia
- Element Plus
- Leaflet
- CSS / SCSS
- Mock 静态数据

## Agent 设计

项目包含 6 个 Agent：

1. `ui_requirement_analyst`  
   分析用户项目计划书，提取 WebGIS 应用主题、页面结构和功能边界。

2. `style_analyst`  
   分析 UI 偏好、参考图片说明、色彩、字体、组件风格。

3. `layout_designer`  
   根据项目需求和 UI 风格设计页面布局。

4. `vue_ui_generator`  
   调用 `WriteProjectFileTool`，真正生成 Vue 前端项目文件。

5. `ui_code_reviewer`  
   审查生成的前端项目结构、运行风险和 UI 一致性。

6. `codex_prompt_writer`  
   生成后续交给 Codex 的修改提示词。

## 核心亮点

- 支持从自然语言项目计划书生成 WebGIS UI 原型
- Agent 不写死固定 UI 风格，而是从用户输入中提取视觉偏好
- 使用自定义文件写入工具生成真实前端工程
- 输出结果可直接运行、预览、继续交给 Codex 修改
- 适合作为 GIS 开发、AI Agent 工程化、前端原型生成方向的个人项目

## 输入文件

项目输入位于：

```text
inputs/project_plan.txt
```

该文件应包含：

```text
1. WebGIS 项目计划书
2. UI 偏好提示词 / 参考图片说明
```

## 输出结果

CrewAI 运行后会生成：

```text
outputs/
├── ui_requirement_analysis.md
├── ui_style_analysis.md
├── layout_plan.md
├── vue_ui_review_report.md
├── codex_prompts/
│   └── codex_next_steps.md
└── generated_frontend/
    ├── package.json
    ├── index.html
    ├── vite.config.ts
    ├── tsconfig.json
    └── src/
```

其中 `outputs/generated_frontend` 是真正可运行的 Vue 前端项目。

## 运行 CrewAI

在项目根目录执行：

```powershell
uv run webgis_ui_prototype
```

## 启动生成的前端项目

```powershell
cd outputs/generated_frontend
npm install
npm run dev
```

然后在浏览器打开 Vite 提供的本地地址。

## 当前阶段边界

当前阶段只生成纯前端 WebGIS UI 原型。

暂不实现：

- 后端接口
- GeoServer 接入
- PostGIS 接入
- Cesium 三维地图
- 登录权限系统
- 复杂业务流程

这些能力会在后续阶段交给 Codex 继续扩展。

## 后续计划

- 引入 Flow，实现生成—检查—反馈—修复循环
- 增加多模型分工，例如分析模型、代码模型、审查模型
- 支持参考图片输入和多模态 UI 分析
- 增加前端实时生成进度展示
- 接入真实 WebGIS 数据服务
