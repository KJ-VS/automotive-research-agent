"""
Statistics Panel

Displays research statistics and
search analytics.

Version
-------
V1.3
"""

import streamlit as st


def show_statistics(result):

    st.subheader("Research Statistics")

    if not result:

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Retrieved", "-")
        col2.metric("Downloaded", "-")
        col3.metric("Time", "-")
        col4.metric("Status", "-")

        return

    statistics = result.get(
        "statistics",
        {}
    )

    analytics = result.get(
        "analytics",
        {}
    )

    # =====================================================
    # Research Statistics
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(

        "Retrieved",

        statistics.get(

            "retrieved",

            0

        )

    )

    col2.metric(

        "Downloaded",

        statistics.get(

            "downloaded",

            0

        )

    )

    col3.metric(

        "Time (s)",

        statistics.get(

            "time",

            0

        )

    )

    col4.metric(

        "Status",

        result.get(

            "status",

            "-"

        )

    )

    st.divider()

    # =====================================================
    # Search Analytics
    # =====================================================

    st.subheader("Search Analytics")

    col1, col2, col3 = st.columns(3)

    col1.metric(

        "Average Score",

        analytics.get(

            "average_score",

            0

        )

    )

    col2.metric(

        "Top Score",

        analytics.get(

            "top_score",

            0

        )

    )

    col3.metric(

        "Best Domain",

        analytics.get(

            "best_domain",

            "-"

        )

    )

    col4, col5 = st.columns(2)

    col4.metric(

        "Avg Domain",

        analytics.get(

            "average_domain_score",

            0

        )

    )

    col5.metric(

        "Avg Content",

        f"{analytics.get('average_content_length',0)} chars"

    )