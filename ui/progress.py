import streamlit as st


def show_status(result: dict | None):
    """
    Display workflow status.
    """

    st.subheader("Status")

    if result is None:

        st.info("🟢 Ready")

        return

    if result["success"]:

        st.success(f"✅ {result['status']}")

    else:

        st.error(result["message"])