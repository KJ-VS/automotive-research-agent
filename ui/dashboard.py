import streamlit as st


def show_dashboard():

    # ----------------------------------------------------
    # Header
    # ----------------------------------------------------
    title_col, version_col = st.columns([8, 2])

    with title_col:
        st.title("🚗 Automotive Research Dashboard")

    with version_col:
        st.markdown("### ")
        st.markdown("**Version 1.1**")

    st.caption("Rule-Based Research Pipeline")

    st.divider()

    # ----------------------------------------------------
    # Main Layout
    # ----------------------------------------------------

    sidebar, workspace = st.columns([1, 3])

    # ====================================================
    # Left Panel
    # ====================================================

    with sidebar:

        st.subheader("Settings")

        st.selectbox(
            "Search Engine",
            ["DuckDuckGo"]
        )

        st.selectbox(
            "Language",
            ["English", "German"]
        )

        st.slider(
            "Max Results",
            5,
            20,
            10
        )

        st.selectbox(
            "Output",
            ["Markdown", "PDF"]
        )

    # ====================================================
    # Right Panel
    # ====================================================

    with workspace:

        st.subheader("Research Question")

        topic = st.text_input(
            "",
            placeholder="Enter your research topic..."
        )

        if st.button(
            "🚀 Start Research",
            use_container_width=True
        ):
            st.info(f"Research Topic: {topic}")

    st.divider()

    # ----------------------------------------------------
    # Status + Statistics
    # ----------------------------------------------------

    left, right = st.columns([1, 3])

    with left:

        st.subheader("Status")

        st.success("🟢 Ready")

    with right:

        st.subheader("Statistics")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Retrieved", 0)
        c2.metric("Filtered", 0)
        c3.metric("Downloaded", 0)
        c4.metric("Time", "0 s")

    st.divider()

    # ----------------------------------------------------
    # Report
    # ----------------------------------------------------

    report_col, download_col = st.columns([8, 1])

    with report_col:
        st.subheader("Report Preview")

    with download_col:
        st.markdown("### ")
        st.button("📄 Export")

    st.text_area(
        "",
        value="No report generated.",
        height=180,
        disabled=True
    )

    st.divider()

    st.caption("Automotive Research Agent • Version 1.1")