import streamlit as st


def show_sidebar():
    """
    Render the application sidebar.

    Returns
    -------
    dict
        All user selected settings.
    """

    with st.sidebar:

        # =====================================================
        # Header
        # =====================================================

        st.title("⚙️ Settings")
        st.caption("Configure the research pipeline")

        st.divider()

        # =====================================================
        # Search Settings
        # =====================================================

        with st.expander("🔍 Search", expanded=True):

            search_engine = st.selectbox(
                "Search Engine",
                (
                    "DuckDuckGo",
                    "Google (Future)",
                    "Bing (Future)"
                ),
                index=0
            )

            language = st.selectbox(
                "Language",
                (
                    "English",
                    "German",
                    "Chinese"
                ),
                index=0
            )

            search_mode = st.selectbox(
                "Search Mode",
                (
                    "Fast",
                    "Balanced",
                    "Comprehensive"
                ),
                index=1
            )

            max_results = st.slider(
                "Maximum Results",
                min_value=5,
                max_value=30,
                value=10,
                step=5
            )

        # =====================================================
        # Output Settings
        # =====================================================

        with st.expander("📄 Output", expanded=True):

            output_formats = st.multiselect(
                "Output Formats",
                [
                    "Markdown (.md)",
                    "PDF (.pdf)",
                    "Word (.docx)",
                    "HTML (.html)",
                    "JSON (.json)"
                ],
                default=["Markdown (.md)"]
            )

            include_sources = st.checkbox(
                "Include Source URLs",
                value=True
            )

            include_timestamp = st.checkbox(
                "Include Timestamp",
                value=True
            )

        # =====================================================
        # Pipeline
        # =====================================================

        with st.expander("⚙️ Pipeline", expanded=False):

            enable_filter = st.checkbox(
                "Enable Domain Filter",
                value=True
            )

            enable_cache = st.checkbox(
                "Enable Cache",
                value=True
            )

            clean_text = st.checkbox(
                "Clean Extracted Text",
                value=True
            )

        # =====================================================
        # Future AI Configuration
        # =====================================================

        with st.expander("🤖 AI (Coming Soon)", expanded=False):

            st.selectbox(
                "LLM",
                [
                    "Disabled",
                    "Azure OpenAI (V2)",
                    "GPT-5 (Future)"
                ],
                index=0,
                disabled=True
            )

            st.slider(
                "Temperature",
                0.0,
                1.0,
                0.2,
                disabled=True
            )

            st.slider(
                "Top P",
                0.0,
                1.0,
                0.9,
                disabled=True
            )

        # =====================================================
        # About
        # =====================================================

        with st.expander("ℹ️ About", expanded=False):

            st.markdown(
                """
**Automotive Research Agent**

Version **V1.1**

Status:

🚧 Development

---

Current milestone

- Streamlit Dashboard
- Modular UI
- Backend Refactoring
                """
            )

    # =========================================================
    # Return Settings
    # =========================================================

    settings = {

        "search_engine": search_engine,

        "language": language,

        "search_mode": search_mode,

        "max_results": max_results,

        "output_formats": output_formats,

        "include_sources": include_sources,

        "include_timestamp": include_timestamp,

        "enable_filter": enable_filter,

        "enable_cache": enable_cache,

        "clean_text": clean_text

    }

    return settings