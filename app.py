import streamlit as st

from ui.dashboard import show_dashboard


st.set_page_config(
    page_title="Automotive Research Dashboard",
    page_icon="🚗",
    layout="wide"
)

show_dashboard()