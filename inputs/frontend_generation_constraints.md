# Frontend Generation Constraints

## 一、整体目标

生成的 WebGIS UI 原型必须优先保证：

1. 可读性
2. 视觉层次
3. 地图区不被背景网格干扰
4. 右侧图表和预警信息清晰
5. 底部时间轴可操作
6. 整体保持深色科技风，但不能牺牲实用性

---

## 二、文字与可读性约束

1. 页面主要文字字号不得小于 14px。
2. 面板标题字号建议 15px - 16px。
3. 重要数据数字字号建议 22px - 30px。
4. 图表坐标轴文字不得小于 11px。
5. 底部时间轴时间文字不得小于 12px。
6. 不要使用过细字体，正文推荐 font-weight: 500。
7. 次要文本颜色不能过暗，避免深灰、暗绿贴近背景。
8. 次要文本建议使用浅灰蓝色，例如 #8EA4B8、#A9B7C6。

---

## 三、中心地图区约束

1. 中心地图区是视觉核心，不能被高亮网格抢占注意力。
2. 背景网格透明度必须降低。
3. 网格线建议使用低透明度青蓝色。
4. 主网格线和次级网格线要区分层级。
5. 地图区需要有视觉焦点，例如洪水光晕、中心涌动区域、风险区域叠加层。
6. 不要让整个地图区域只有均匀网格。
7. 流体动力学纹理应表现为水流、洪水扩散、半透明涌动效果，不要做成星系粒子聚集效果。

---

## 四、左右面板约束

1. 左右面板不要使用完全实心黑色。
2. 使用半透明深色背景，例如 rgba(5, 12, 22, 0.82)。
3. 面板可以加入轻微 backdrop-filter: blur(10px)。
4. 面板边界不要太生硬，可使用浅蓝低透明边框。
5. 面板之间要有足够内边距，避免文字贴边。
6. 列表项高度不要太矮，推荐 40px - 48px。

---

## 五、右侧图表约束

### 水位趋势图

1. 坐标轴文字必须清晰可见。
2. 坐标轴和网格线透明度适中，不能太暗。
3. 折线下方必须增加渐变填充。
4. 峰值点需要有明显标注。
5. 图表区域需要留足 padding，避免内容贴边。

### 风险分布图

1. 环形图尺寸不能过小。
2. 图例颜色必须和图形颜色一一对应。
3. 图例文字和百分比要对齐。
4. 图例不要过于拥挤。

---

## 六、预警列表约束

1. 预警列表不能文字过密。
2. 每条预警需要卡片化。
3. 高等级预警必须突出显示。
4. 红色 / 橙色预警应带有低透明背景色。
5. 每条预警应包含：
   - 等级标签
   - 时间
   - 地点
   - 简短描述
   - 关键水位值
6. 最高等级预警应该第一眼可见。

---

## 七、工具栏约束

1. 工具按钮点击区域不能过小。
2. 工具按钮推荐最小尺寸 48px x 48px。
3. 图标尺寸不得小于 18px。
4. 当前激活工具要有明显高亮。
5. 按钮之间要有清晰间距。

---

## 八、底部时间轴约束

1. 时间轴是关键组件，不能太细。
2. 底部区域高度建议 72px - 88px。
3. 时间轴轨道必须加粗。
4. 滑块必须明显，方便拖拽。
5. 播放按钮、倍速按钮要足够大。
6. 当前时间点需要突出显示。
7. 事件节点要有颜色和形状区分。

---

## 九、页面结构约束

推荐布局：

- 顶部导航栏：48px - 56px
- 左侧面板：280px - 320px
- 右侧面板：300px - 360px
- 底部时间轴：72px - 88px
- 中心地图区：占据剩余空间

不要让左右面板过宽，也不要让中心地图被压缩。

---

## 十、文件生成约束

必须生成：

```text
outputs/generated_frontend/
├── package.json
├── index.html
├── vite.config.ts
├── tsconfig.json
├── src/main.ts
├── src/App.vue
├── src/router/index.ts
├── src/views/HomeView.vue
├── src/views/MapView.vue
├── src/components/AppHeader.vue
├── src/components/MapPanel.vue
├── src/components/LayerPanel.vue
├── src/components/StatsPanel.vue
├── src/components/WarningPanel.vue
├── src/components/TimelineBar.vue
├── src/stores/dashboardStore.ts
├── src/mock/dashboardMock.ts
└── src/styles/global.css
```

---

## 十一、地图实现约束

当前阶段只生成 WebGIS UI 原型，不接真实地图引擎。

禁止使用：

- vue-leaflet
- @vue-leaflet/vue-leaflet
- Cesium
- OpenLayers
- Mapbox
- 高德地图 API

地图区域必须使用以下方式模拟：

- SVG
- Canvas
- CSS 背景
- mock polygon
- mock point
- mock polyline
- mock heatmap

地图区必须表现出 WebGIS 空间要素，例如：

- 研究区边界
- 风险区 polygon
- 监测点 point
- 巡护路线 polyline
- 图例
- 比例尺
- 坐标信息

不要在 package.json 中添加任何真实地图相关依赖。