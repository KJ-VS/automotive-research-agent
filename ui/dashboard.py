"""
Dashboard UI

Enterprise AI Research Dashboard

Version
-------
V1.3
"""

import streamlit as st

from backend.controller import Controller

from ui.sidebar import show_sidebar
from ui.progress import show_status
from ui.statistics import show_statistics
from ui.report import show_report


def show_dashboard():
    """
    Render the main dashboard.
    """

    # ======================================================
    # Controller
    # ======================================================

    controller = Controller()

    # ======================================================
    # Sidebar
    # ======================================================

    settings = show_sidebar()

    # ======================================================
    # Header
    # ======================================================

    title_col, version_col = st.columns([8, 2])

    with title_col:

        st.title("🚗 Automotive Research Dashboard")

        st.caption(
            "Enterprise AI Research Platform"
        )

    with version_col:

        st.markdown("###")

        st.info("🚀 V1.3")

    st.divider()

    # ======================================================
    # Research Question
    # ======================================================

    st.subheader("Research Question")

    research_question = st.text_area(

        label="",

        placeholder="What would you like to research today?",

        height=140

    )

    # ======================================================
    # Execute Research
    # ======================================================

    result = None

    if st.button(

        "🚀 Start Research",

        use_container_width=True,

        type="primary"

    ):

        if not research_question.strip():

            st.warning(
                "Please enter a research question."
            )

        else:

            with st.spinner(

                "Running enterprise research workflow..."

            ):

                result = controller.start_research(

                    query=research_question,

                    settings=settings

                )

    # ======================================================
    # Status
    # ======================================================

    show_status(result)

    st.divider()

    # ======================================================
    # Statistics
    # ======================================================

    show_statistics(result)

    st.divider()

    # ======================================================
    # Report
    # ======================================================

    show_report(result)

    st.divider()

    # ======================================================
    # Footer
    # ======================================================

    st.caption(

        "© 2026 Automotive Research Agent | Enterprise AI Platform | Version 1.3"

    )