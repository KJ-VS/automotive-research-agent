import streamlit as st


def show_report():
    """
    Display report preview.
    """

    st.subheader("Markdown Preview")

    preview = st.empty()

    preview.info(
        """
No report generated yet.

Click **Start Research** to generate a report.
"""
    )

    st.button(
        "📄 Export",
        disabled=True
    )