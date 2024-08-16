import streamlit as st
import pandas as pd

def show_explore_page():
    st.title("Data Exploration - Heart Disease")

    # Load dataset
    df = pd.read_csv("heart.csv")

    st.write("## Dataset Overview")
    st.write(df.head())

    st.write("### Basic Statistics")
    st.write(df.describe())

    st.write("### Class Distribution (Heart Disease)")
    st.bar_chart(df["HeartDisease"].value_counts())

    st.write("### Chest Pain Type Distribution")
    st.bar_chart(df["ChestPainType"].value_counts())

