"""
Design Tokens 结构化模型

这是 vision_extractor agent 的输出格式。
将参考图片中的视觉信息"翻译"为下游 agent 可以直接使用的 JSON 数据。

设计原则：
1. 字段必须可枚举或可量化，避免自由文本（避免 LLM 输出走样）
2. 每个字段都附详细 description，agent 才知道怎么填
3. 必填字段用默认值兜底，避免 agent 偷懒漏填
"""

from typing import List, Literal, Optional
from pydantic import BaseModel, Field


class ColorPalette(BaseModel):
    """配色方案"""

    background_primary: str = Field(
        description="主背景色，必须是 #RRGGBB 格式的十六进制色值，如 #2B1810",
    )
    background_secondary: str = Field(
        description="次背景色（卡片、面板背景），#RRGGBB 格式",
    )
    accent_primary: str = Field(
        description="主强调色（按钮、标题、关键描边），#RRGGBB 格式",
    )
    accent_secondary: str = Field(
        description="次强调色（辅助高亮、次要按钮），#RRGGBB 格式",
    )
    text_primary: str = Field(
        description="主要文字颜色，#RRGGBB 格式",
    )
    text_secondary: str = Field(
        description="次要文字颜色（说明文字、占位符），#RRGGBB 格式",
    )
    semantic_success: Optional[str] = Field(
        default=None,
        description="语义色-成功/正常状态，#RRGGBB 格式，无则填 null",
    )
    semantic_warning: Optional[str] = Field(
        default=None,
        description="语义色-警告状态，#RRGGBB 格式，无则填 null",
    )
    semantic_danger: Optional[str] = Field(
        default=None,
        description="语义色-危险/错误状态，#RRGGBB 格式，无则填 null",
    )


class Typography(BaseModel):
    """字体排版"""

    font_family_heading: str = Field(
        description="标题字体族，如 'Press Start 2P, monospace' 或 'Inter, sans-serif'",
    )
    font_family_body: str = Field(
        description="正文字体族，如 'Courier Prime, monospace'",
    )
    font_weight_heading: int = Field(
        description="标题字重，100-900 之间的整数，例如 700 表示粗体，200 表示极细",
        ge=100,
        le=900,
    )
    font_weight_body: int = Field(
        description="正文字重，100-900 之间的整数",
        ge=100,
        le=900,
    )
    font_size_base_px: int = Field(
        description="基础字号（像素），如 14、16、18。儿童产品建议 18+，专业产品 14",
        ge=10,
        le=32,
    )
    letter_spacing_style: Literal["tight", "normal", "wide", "very_wide"] = Field(
        description="字间距风格：tight=紧凑（现代极简），normal=正常，wide=宽松（科技感），very_wide=极宽（复古打字机）",
    )


class LayoutShape(BaseModel):
    """形状与轮廓"""

    border_radius_px: int = Field(
        description="圆角大小（像素）。0=硬朗直角（工业风/复古），4-8=轻微圆角（专业），12-20=中等（现代SaaS），24+=圆润（卡通/儿童）",
        ge=0,
        le=64,
    )
    border_width_px: int = Field(
        description="描边粗细（像素）。0=无边框（毛玻璃/极简），1-2=细描边（现代），3-5=粗描边（复古工业/卡通）",
        ge=0,
        le=8,
    )
    shadow_style: Literal["none", "subtle", "soft_glow", "hard_pixel", "neumorphism"] = Field(
        description="阴影风格：none=无阴影，subtle=柔和投影，soft_glow=发光（科技风），hard_pixel=硬像素阴影（复古），neumorphism=新拟物",
    )
    information_density: Literal["minimal", "standard", "rich"] = Field(
        description="信息密度：minimal=极简（大量留白，元素少），standard=标准，rich=信息密集（仪表盘风格）",
    )


class VisualMood(BaseModel):
    """视觉氛围"""

    overall_temperature: Literal["warm", "neutral", "cool"] = Field(
        description="色温倾向：warm=暖色（橙红黄），neutral=中性（灰白黑），cool=冷色（蓝青紫）",
    )
    brightness_level: Literal["very_dark", "dark", "medium", "light", "very_light"] = Field(
        description="整体明度：very_dark=纯黑深色，dark=深色（科技仪表盘），medium=中等，light=浅色（专业SaaS），very_light=极浅（卡通儿童）",
    )
    style_keywords: List[str] = Field(
        description="3-7 个风格关键词，要具体可描述，如 ['复古工业', '航海控制台', '70年代', '机械感']。禁止用通用词如 '现代' '美观'",
        min_length=3,
        max_length=7,
    )
    decoration_elements: List[str] = Field(
        default_factory=list,
        description="装饰性视觉元素列表，如 ['网格背景', '雷达扫描环', '螺丝铆钉', '扫描线动画']。无装饰则给空列表 []",
    )
    forbidden_styles: List[str] = Field(
        default_factory=list,
        description="禁止使用的风格列表（用户明确拒绝的）。如 ['毛玻璃', '深色背景', '冷色调']。无则给空列表 []",
    )


class LayoutPattern(BaseModel):
    """布局模式"""

    primary_pattern: Literal[
        "sidebar_left",
        "sidebar_right",
        "sidebar_both",
        "top_bottom",
        "card_grid",
        "stacked",
        "fullscreen_canvas",
    ] = Field(
        description="主布局模式：sidebar_*=侧边栏式，top_bottom=上下分层，card_grid=卡片网格，stacked=单列堆叠，fullscreen_canvas=全屏画布",
    )
    has_top_bar: bool = Field(description="是否有顶部状态/导航栏")
    has_bottom_bar: bool = Field(description="是否有底部状态/工具栏")
    main_content_ratio: float = Field(
        description="主内容区占整个布局的比例（0.0-1.0）。地图主导=0.6-0.7，仪表盘=0.5-0.6，内容堆叠=0.8+",
        ge=0.3,
        le=1.0,
    )


class DesignTokens(BaseModel):
    """
    完整的视觉设计令牌
    
    这是 vision_extractor agent 的最终输出。
    所有下游 agent (style_analyst, layout_designer, vue_ui_generator) 
    都会基于这个对象工作，不再需要自由文本描述。
    """

    source_type: Literal["image", "text", "hybrid"] = Field(
        description="来源类型：image=主要从图片提取，text=只有文字描述，hybrid=图文结合",
    )
    confidence: Literal["high", "medium", "low"] = Field(
        description="提取置信度：high=信息充分，medium=部分推断，low=高度依赖默认值",
    )
    color_palette: ColorPalette
    typography: Typography
    layout_shape: LayoutShape
    visual_mood: VisualMood
    layout_pattern: LayoutPattern
    extraction_notes: str = Field(
        description="提取过程的关键说明：从图片/文字中提取了什么、推断了什么、用户明确禁止了什么。1-3 句话",
        max_length=500,
    )
