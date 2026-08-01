import streamlit as st

from ui.sidebar import show_sidebar
from ui.progress import show_status
from ui.statistics import show_statistics
from ui.report import show_report


def show_dashboard():

    # ==========================================
    # Sidebar
    # ==========================================

    settings = show_sidebar()

    # ==========================================
    # Header
    # ==========================================

    title_col, version_col = st.columns([8, 2])

    with title_col:

        st.title("🚗 Automotive Research Dashboard")
        st.caption("Enterprise AI Research Platform")

    with version_col:

        st.markdown("###")
        st.success("V1.1")

    st.divider()

    # ==========================================
    # Research Question
    # ==========================================

    st.subheader("Research Question")

    research_question = st.text_area(
        label="",
        placeholder="What would you like to research today?",
        height=140
    )

    start_button = st.button(
        "🚀 Start Research",
        use_container_width=True,
        type="primary"
    )

    # ==========================================
    # Temporary Debug
    # ==========================================

    if start_button:

        st.toast("Research pipeline will start here.")

        with st.expander("Current Settings"):

            st.json(settings)

            st.write("Question:")

            st.write(research_question)

    st.divider()

    # ==========================================
    # Status
    # ==========================================

    show_status()

    st.divider()

    # ==========================================
    # Statistics
    # ==========================================

    show_statistics()

    st.divider()

    # ==========================================
    # Report Preview
    # ==========================================

    show_report()

    st.divider()

    st.caption(
        "© 2026 Automotive Research Agent | Version 1.1"
    )