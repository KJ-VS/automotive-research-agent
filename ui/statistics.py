import streamlit as st


def show_statistics(statistics: dict | None):
    """
    Display workflow statistics.
    """

    st.subheader("Statistics")

    if statistics is None:

        statistics = {

            "retrieved": 0,
            "filtered": 0,
            "downloaded": 0,
            "time": 0

        }

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Retrieved",
            statistics["retrieved"]
        )

    with col2:

        st.metric(
            "Filtered",
            statistics["filtered"]
        )

    with col3:

        st.metric(
            "Downloaded",
            statistics["downloaded"]
        )

    with col4:

        st.metric(
            "Time",
            f"{statistics['time']} s"
        )