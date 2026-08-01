import streamlit as st


def show_statistics():
    """
    Display research statistics.
    """

    st.subheader("Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Retrieved",
            value=0
        )

    with col2:
        st.metric(
            label="Filtered",
            value=0
        )

    with col3:
        st.metric(
            label="Downloaded",
            value=0
        )

    with col4:
        st.metric(
            label="Time",
            value="0 s"
        )