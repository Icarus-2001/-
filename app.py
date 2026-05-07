"""
美甲AI试戴与智能运营系统 — Streamlit 应用骨架
"""

import time

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="美甲视界 - AI与运营中枢",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----- 左侧边栏 -----
with st.sidebar:
    st.header("项目简介")
    st.markdown(
        """
**美甲视界** 旨在融合 **AI 试戴体验** 与 **智能运营决策**，为 C 端用户提供沉浸式美甲预览，
为 B 端运营提供数据洞察与策略辅助。当前页面为系统骨架，后续将接入大模型与业务模块。
        """
    )
    st.divider()
    st.subheader("API 配置（预留）")
    api_key = st.text_input(
        "API Key",
        type="password",
        placeholder="后续接入 AI 大模型时填写",
        help="密钥仅保存在当前会话内存中，刷新页面后需重新输入。",
        label_visibility="visible",
    )
    if api_key:
        st.caption("已输入密钥（会话内有效）")

# ----- 主体 -----
st.title("美甲视界 - AI与运营中枢")

tab_tryon, tab_ops = st.tabs(["C端体验：AI试戴", "B端管控：智能运营看板"])

with tab_tryon:
    col_left, col_right = st.columns([1, 1])
    with col_left:
        uploaded_file = st.file_uploader(
            "上传您的手部照片 (支持 JPG/PNG)",
            type=["jpg", "jpeg", "png"],
            help="请上传清晰的正面手部照片以便试戴演示。",
        )
        nail_style = st.selectbox(
            "选择美甲款式",
            ("法式冰透", "猫眼渐变", "金属朋克", "日系手绘"),
        )
        generate_clicked = st.button("✨ 生成AI试戴效果")

    with col_right:
        if generate_clicked:
            if uploaded_file is None:
                st.warning("请先上传手部照片")
            else:
                with st.spinner("AI正在进行手型识别与款式融合..."):
                    time.sleep(2)
                st.success(
                    "试戴完成！当前手型与款式匹配度：98%（此为演示占位）"
                )
                st.image(
                    "https://images.unsplash.com/photo-1522337660859-02fbefca4702?w=500&q=80",
                    caption="AI生成的试戴效果图",
                    use_container_width=True,
                )
        else:
            st.info(
                "👈 请在左侧上传照片并选择款式，点击生成即可查看试戴效果。"
            )

with tab_ops:
    ops_df = pd.DataFrame(
        {
            "款式名称": ["法式冰透", "猫眼渐变", "金属朋克", "日系手绘", "纯色极简"],
            "浏览量": [1200, 3500, 800, 2100, 1500],
            "试戴次数": [850, 2900, 150, 1100, 400],
            "最终转化率": ["12.5%", "28.3%", "2.1%", "8.4%", "5.0%"],
        }
    )

    st.subheader("📊 实时业务数据大盘")
    st.dataframe(ops_df, use_container_width=True, hide_index=True)

    fig_tryon = px.bar(
        ops_df,
        x="款式名称",
        y="试戴次数",
        title="各款式试戴热度排行",
    )
    st.plotly_chart(fig_tryon, use_container_width=True)

    st.divider()
    st.subheader("🧠 openclaw 智能趋势诊断")
    analyze_clicked = st.button(
        "执行全盘数据分析与策略生成",
        type="primary",
        key="ops_full_analysis",
    )

    if analyze_clicked:
        with st.spinner(
            "openclaw 正在深度读取大盘点击率、试戴率，比对全网趋势..."
        ):
            time.sleep(2)
        st.success(
            """
**【异常预警】** “金属朋克”款式的浏览量有 800，但试戴率不足 20%，转化率极低，疑似详情页图片与真实肤色匹配度差。

**【爆款预测】** 结合试戴漏斗分析，“猫眼渐变”转化效率极高，且外部社交平台热度呈上升趋势，判定为本周 S 级爆款。

**【运营动作建议】** 建议将“猫眼渐变”置顶至首页 C 位；针对“金属朋克”触发降价清仓或优化 AI 试戴光影算法。
            """.strip()
        )
