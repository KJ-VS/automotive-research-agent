import streamlit as st


def show_report(report: str | None):
    """
    Display report preview.
    """

    st.subheader("Markdown Preview")

    if not report:

        st.info(
            """
No report generated yet.

Click **Start Research** to begin.
"""
        )

    else:

        st.markdown(report)

    st.button(

        "📄 Export",

        disabled=(report is None)

    )