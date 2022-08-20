# Contents of ~/my_app/streamlit_app.py
import streamlit as st

def main_page():
    st.markdown("# Landing page 🎈")
    st.sidebar.markdown("# Landing page 🎈")

def page2():
    st.markdown("# Measurements ❄️")
    st.sidebar.markdown("# Measurements ❄️")

def page3():
    st.markdown("# Predictions 🎉")
    st.sidebar.markdown("# Predictions 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
