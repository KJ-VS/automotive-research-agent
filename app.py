import streamlit as st

from ui.dashboard import show_dashboard


st.set_page_config(
    page_title="Automotive Research Agent",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)


def main():

    show_dashboard()


if __name__ == "__main__":
    main()