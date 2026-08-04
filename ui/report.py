"""
Report View

Displays the generated research report and
search result details.

Version
-------
V1.3
"""

import streamlit as st


def show_report(result):

    st.subheader("Research Report")

    if not result:

        st.info(
            "No report available.\n\n"
            "Click **Start Research** to begin."
        )

        return

    # =====================================================
    # Markdown Report
    # =====================================================

    report = result.get(
        "report",
        ""
    )

    st.markdown(report)

    st.divider()

    # =====================================================
    # Search Results
    # =====================================================

    st.subheader("Ranked Search Results")

    pages = result.get(
        "pages",
        []
    )

    if not pages:

        st.warning(
            "No search results available."
        )

        return

    for page in pages:

        title = page.get(
            "title",
            "Unknown"
        )

        rank = page.get(
            "rank",
            "-"
        )

        overall = page.get(
            "overall_score",
            0
        )

        with st.expander(

            f"#{rank}  {title}"

        ):

            # ==========================================
            # Score Overview
            # ==========================================

            col1, col2, col3 = st.columns(3)

            col1.metric(

                "Overall",

                f"{overall}/100"

            )

            col2.metric(

                "Domain",

                page.get(
                    "domain_score",
                    0
                )

            )

            col3.metric(

                "Rank",

                rank

            )

            st.divider()

            # ==========================================
            # Detailed Scores
            # ==========================================

            c1, c2 = st.columns(2)

            with c1:

                st.metric(

                    "Title Score",

                    page.get(
                        "title_score",
                        0
                    )

                )

                st.metric(

                    "Snippet Score",

                    page.get(
                        "snippet_score",
                        0
                    )

                )

            with c2:

                st.metric(

                    "Content Score",

                    page.get(
                        "content_score",
                        0
                    )

                )

                st.metric(

                    "Penalty",

                    page.get(
                        "penalty",
                        0
                    )

                )

            # ==========================================
            # Metadata
            # ==========================================

            st.markdown("### URL")

            st.code(

                page.get(
                    "url",
                    ""
                ),

                language=None

            )

            category = page.get(
                "category",
                "General"
            )

            st.markdown(
                f"**Category:** {category}"
            )

            # ==========================================
            # Summary
            # ==========================================

            st.markdown("### Summary")

            st.write(

                page.get(
                    "summary",
                    ""
                )

            )

            # ==========================================
            # Ranking Explanation
            # ==========================================

            reasons = page.get(
                "reason",
                []
            )

            if reasons:

                st.markdown(
                    "### Why was this ranked here?"
                )

                for item in reasons:

                    st.success(item)

    st.divider()

    st.download_button(

        label="📄 Download Markdown Report",

        data=result.get(
            "report",
            ""
        ),

        file_name="research_report.md",

        mime="text/markdown"
    )