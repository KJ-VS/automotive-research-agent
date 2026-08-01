import streamlit as st


def show_status():
    """
    Display current pipeline status.

    Returns
    -------
    streamlit.delta_generator.DeltaGenerator
        Placeholder for updating status dynamically.
    """

    st.subheader("Status")

    status_placeholder = st.empty()

    status_placeholder.success("🟢 Ready")

    return status_placeholder