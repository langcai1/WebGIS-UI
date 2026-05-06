# WebGIS UI Prototype Generator

> 基于 CrewAI 多智能体协作的 WebGIS 前端 UI 原型生成器。输入项目计划书与 UI 偏好，自动产出可运行的 Vue 3 前端原型。

<p align="center">
  <img src="https://img.shields.io/badge/CrewAI-1.14.3-blue" />
  <img src="https://img.shields.io/badge/Python-3.10+-green" />
  <img src="https://img.shields.io/badge/Vue-3.4-brightgreen" />
  <img src="https://img.shields.io/badge/TypeScript-5.5-blue" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

---

## ✨ 项目亮点

**同一套多智能体配置，8 种风格迥异的 WebGIS UI 原型，全部由用户输入驱动。**

| 项目 | 风格 | 截图 |
|------|------|------|
| 火星任务控制台 | NASA 复古科技（CRT 扫描线、琥珀绿） | `examples/02_mars_mission/` |
| 1888 房产报刊 | 复古黑白报刊（衬线字体、印章装饰） | `examples/05_estate_gazette/` |
| 松风阁茶室 | 极简东方禅意（留白、墨黑印泥红） | `examples/03_tea_house/` |
| NOVA 电竞观战 | 赛博朋克霓虹（紫粉荧光） | `examples/04_esports_arena/` |
| 城市地铁监测 | 深色科技仪表盘 | `examples/08_metro_monitor/` |
| 森林健康监测 | 自然系绿色（多页面） | `examples/01_forest_health/` |
| 城市急救调度 | 医疗严肃（红蓝白） | `examples/06_emergency_dispatch/` |
| 珊瑚岛旅游导览 | 清新海岛（暖橙青蓝） | `examples/07_coral_island/` |

---

## 🎯 解决了什么问题

通用的 UI 生成工具在 WebGIS 这种**专业垂直领域**表现一般——它们不懂图层管理、不懂坐标系、生成的地图组件经常无法运行。

本项目针对 WebGIS 场景做了三件事：

1. **垂直领域知识库**：在 agent backstory 中内置了监测预警、数据可视化、业务办公、公共服务四类 GIS 应用的标准组件库
2. **多智能体协作链路**：从需求分析、视觉提取、布局设计到代码生成、代码审查，7 个 agent 各司其职
3. **结构化视觉契约**：通过 Pydantic 模型强制视觉信息无损传递，避免下游 agent "脑补"

---

## 🏗️ 系统架构

```
┌──────────────┐
│   用户输入   │  project_plan.txt + (可选) reference_image.png
└──────┬───────┘
       │
       ▼
┌─────────────────────────────────────────────────────┐
│   Stage 1: 视觉令牌提取                              │
│   vision_extractor (GPT-4o, multimodal)             │
│   → 输出 DesignTokens (JSON, Pydantic 强约束)       │
└──────┬──────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────┐
│   Stage 2: 需求与风格分析                            │
│   ui_requirement_analyst → 提取页面/功能/数据需求    │
│   style_analyst         → 细化前端风格规范           │
└──────┬──────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────┐
│   Stage 3: 布局与代码生成                            │
│   layout_designer  → 设计页面布局                    │
│   vue_ui_generator → 生成 Vue 3 + TypeScript 代码    │
└──────┬──────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────┐
│   Stage 4: 审查与交付                                │
│   ui_code_reviewer       → 审查代码与设计一致性      │
│   codex_prompt_writer    → 生成后续迭代提示词         │
└──────┬──────────────────────────────────────────────┘
       │
       ▼
   可运行的 Vue 3 项目 + 完整设计文档
```

### Agent 分工详解

| Agent | LLM | 职责 | 输出 |
|-------|-----|------|------|
| `vision_extractor` | GPT-4o (multimodal) | 提取视觉令牌（颜色/字体/圆角/布局） | `design_tokens.json` |
| `ui_requirement_analyst` | DeepSeek-chat | 解析项目主题与功能需求 | `ui_requirement_analysis.md` |
| `style_analyst` | DeepSeek-chat | 把视觉令牌翻译为前端样式规范 | `ui_style_analysis.md` |
| `layout_designer` | DeepSeek-chat | 设计页面布局结构 | `layout_plan.md` |
| `vue_ui_generator` | DeepSeek-chat | 生成完整 Vue 3 项目代码 | `vue_ui_project_plan.md` |
| `ui_code_reviewer` | DeepSeek-chat | 审查代码并对比上游设计 | `vue_ui_review_report.md` |
| `codex_prompt_writer` | DeepSeek-chat | 生成后续迭代的 Codex 提示词 | `codex_next_steps.md` |

### 工程优化亮点

- **混合 LLM 路由**：仅 1 个 agent 使用昂贵的多模态模型 (GPT-4o)，其他 6 个使用经济的 DeepSeek-chat，**单次成本控制在 ¥0.05–0.16**
- **视觉契约层**：Pydantic 模型 `DesignTokens` 作为视觉信息的中间表示，避免自然语言描述带来的精度损失
- **可复现性**：CrewAI 版本固定，结构化 JSON 输出可校验

---

## 📊 实测数据

实测 8 个项目的运行数据（基于 DeepSeek-chat + GPT-4o 混合路由）：

| 项目 | 总耗时 | Token 成本 | 风格还原度（自评） |
|------|--------|-----------|-------------------|
| 森林健康监测 | 15 min | ¥0.13 | 9/10 |
| 火星任务控制台 | 11 min | ¥0.05 | 10/10 |
| 松风阁茶室 | 10 min | ¥0.16 | 8/10 |
| 城市地铁监测 | 13 min | ¥0.12 | 9/10 |
| NOVA 电竞观战 | 11 min | ¥0.07 | 9/10 |
| 1888 房产报刊 | 6 min | ¥0.06 | 9/10 |
| 城市急救调度 | 11min | –¥0.07 | 9/10 |
| 珊瑚岛旅游导览 | 10min | – | 8/10 |
| **平均** | **≈ 11 min** | **≈ ¥0.10** | **9/10** |

---

## 🚀 快速开始

### 环境要求

- Python 3.10–3.13
- Node.js 18+ (用于运行生成的 Vue 项目)
- [uv](https://docs.astral.sh/uv/) (Python 包管理器)

### 安装

```bash
# 克隆仓库
git clone https://github.com/langcai1/webgis-ui-prototype-generator.git
cd webgis-ui-prototype-generator

# 安装依赖
uv sync
# 或
crewai install
```

### 配置 API Key

复制 `.env.example` 为 `.env`，填入以下任一组合：

```env
# 方案 A：仅使用 DeepSeek（不支持图片输入）
OPENAI_API_KEY=<你的 deepseek key>
OPENAI_BASE_URL=https://api.deepseek.com
OPENAI_MODEL_NAME=deepseek-chat

# 方案 B：DeepSeek + OpenAI 混合（推荐，支持图片输入）
DEEPSEEK_API_KEY=<你的 deepseek key>
OPENAI_API_KEY=<你的 openai key>  # 仅 vision_extractor 使用
```

### 运行

```bash
# 1. 准备输入
echo "你的项目计划书..." > inputs/project_plan.txt



# 2. 启动 crew
crewai run

# 3. 查看输出
ls outputs/
# - design_tokens.json          ← 提取的视觉令牌
# - ui_requirement_analysis.md  ← 需求分析
# - ui_style_analysis.md        ← 风格规范
# - layout_plan.md              ← 布局设计
# - vue_ui_project_plan.md      ← 完整 Vue 项目方案
# - vue_ui_review_report.md     ← 代码审查报告
# - codex_prompts/              ← 后续迭代提示词

# 4. 运行生成的前端
cd outputs/generated_frontend
npm install
npm run dev
```

---

## 📁 项目结构

```
webgis-ui-prototype-generator/
├── src/webgis_ui_prototype/
│   ├── config/
│   │   ├── agents.yaml          # 7 个 agent 的角色与背景
│   │   └── tasks.yaml           # 7 个 task 的描述与依赖
│   ├── tools/                   # 自定义工具（预留）
│   ├── crew.py                  # Crew 装配
│   └── main.py                  # 入口与 inputs 处理
├── inputs/
│   ├── project_plan.txt         # 用户输入：项目计划书
│   └── reference_image.png      # 用户输入：可选参考图
├── outputs/
│   └── ...                      # 7 个 agent 的产出文件
├── examples/                    # 8 个完整运行案例
│   ├── 01_forest_health/
│   ├── 02_mars_mission/
│   └── ...
├── pyproject.toml
└── README.md
```

---

## 🎨 Examples Gallery

每个案例都包含完整的**输入 + 中间产物 + 最终截图**，可在 `examples/` 目录查看。

### 1. 森林健康监测中心
> 自然系绿色 · 多页面 · 大兴安岭林区

![Forest Dashboard](examples/01_forest_health/screenshots/dashboard.png)

特点：4 个完整页面（首页总览 / 监测地图 / 任务管理 / 关于系统）、包含面积统计、风险分布饼图、实时预警、林区健康趋势曲线。

### 2. 火星任务控制台 ⭐
> NASA 70 年代复古科技 · CRT 扫描线 · 琥珀绿单色终端

![Mars Mission](examples/02_mars_mission/screenshots/main.png)

特点：致敬阿波罗任务控制台美学、命令日志终端、遥测数据流、任务进度追踪、`T+01:24:02` 任务时间格式。

### 3. 松风阁茶室
> 极简东方禅意 · 宣纸白底 · 墨黑印泥红

![Tea House](examples/03_tea_house/screenshots/main.png)

特点：极致克制的信息密度、衬线标题、4 个独立大卡片、印章装饰、"午时 12:13"古典时间表达。

### 4. NOVA 电竞观战
> 赛博朋克霓虹 · 紫粉荧光 · 高信息密度

![Esports](examples/04_esports_arena/screenshots/main.png)

特点：双方选手数据面板、地图战术视图、HP/MP 血条、实时预警、KDA 统计、底部事件流。

### 5. 1888 房产报刊 ⭐⭐
> 复古黑白报刊 · 衬线字体 · 印章装饰

![Estate Gazette](examples/05_estate_gazette/screenshots/main.png)

特点：报头风格标题、Vol. LXXXII 罗马数字版次、印章 SVG 装饰、灰度地图风格、左侧分类筛选 + 右侧市场报告。

### 6. 城市急救中心
> 医疗严肃 · 红蓝白 · 高密度信息列表

![Emergency](examples/06_emergency_dispatch/screenshots/main.png)

特点：实时报警事件列表、医院床位资源进度条、严肃克制无装饰、空闲/出勤状态标签。

### 7. 珊瑚岛旅游导览
> 清新海岛 · 卡通 emoji 图标 · 推荐路线

![Coral Island](examples/07_coral_island/screenshots/main.png)

特点：海岛俯视图、emoji 景点图标、左侧分类筛选、底部精选路线卡片、实时承载率展示。

### 8. 城市地铁监测中心
> 深色科技仪表盘 · 多页面 · 多线路图

![Metro](examples/08_metro_monitor/screenshots/dashboard.png)

特点：5 条地铁线路可视化、站点拥挤度排行、ECharts 趋势图、站点详情子页面、实时进出站数据。

---

## ⚠️ Known Limitations

诚实地列出当前项目的局限：

1. **像素级复刻不支持**：本项目做"风格迁移"，不做"截图复刻"。给定参考图，输出的是**风格相似的全新设计**，不是 1:1 重现。

2. **Generator 偶有越权**：在某些案例中，`vue_ui_generator` 会主动添加 `layout_designer` 未规划的组件（如预警面板、统计卡片）。原因是 LLM 训练数据中"标准 SaaS dashboard"的先验过强。**优化方向**：引入 Generator-Reviewer 反馈循环（基于 CrewAI Flow 的 router 机制）。

3. **生成的代码需要后续打磨**：第一版代码可直接 `npm run dev` 运行，但部分场景下存在小问题（如 Element Plus 图标未导入、自定义字体加载延迟）。`codex_prompt_writer` 的输出可用于后续 IDE Agent 自动修复。

4. **多模态 agent 的成本**：图片输入需要 GPT-4o 支持，单次额外成本约 ¥0.03-0.05。当前默认配置下，无图片输入时仅使用 DeepSeek，成本最低。

---

## 🛠️ 技术栈

**后端 (Crew)**：
- CrewAI 1.14.3
- Python 3.10+
- DeepSeek-chat (主力 LLM)
- GPT-4o (视觉理解，可选)
- Pydantic (结构化输出)

**前端 (生成产物)**：
- Vue 3.4 + TypeScript 5.5
- Vite 5.4
- Pinia 2.x
- Element Plus
- Leaflet (预留地图引擎)

---

## 🗺️ Roadmap

- [ ] 引入 Generator-Reviewer 反馈循环（Flow + router）
- [ ] 基于截图的多模态视觉对比反馈
- [ ] Web UI（前端可视化输入界面 + Agent 协作过程实时展示）
- [ ] 支持更多前端框架（React、Svelte）
- [ ] 接入真实 Leaflet/Mapbox 地图引擎模板

---

## 📄 License

MIT License — 自由使用、修改、分发，欢迎贡献。

---

## 🙏 致谢

- [CrewAI](https://crewai.com) — 多智能体编排框架
- [DeepSeek](https://www.deepseek.com) — 高性价比的中文 LLM
- 所有提供 prompt 灵感的开源 UI 设计参考

---

如果这个项目对你有帮助，欢迎 ⭐ Star。问题反馈与 PR 都欢迎。
