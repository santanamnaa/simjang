import streamlit as st
from explore_page import show_explore_page
from predict_page import show_predict_page

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ("Explore Data", "Make Predictions"))

if page == "Explore Data":
    show_explore_page()
else:
    show_predict_page()
