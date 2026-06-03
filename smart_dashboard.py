import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Data Dashboard", layout="wide")

st.title("📊 Smart Data Dashboard with Insights")

# Upload file
file = st.file_uploader("Upload your CSV file", type=["csv"])

if file is not None:
    df = pd.read_csv(file)

    st.subheader("📌 Data Preview")
    st.write(df.head())

    st.subheader("📊 Basic Info")
    st.write(df.describe())

    # Select column for analysis
    numeric_cols = df.select_dtypes(include=['number']).columns

    if len(numeric_cols) > 0:
        col = st.selectbox("Select numeric column", numeric_cols)

        # Chart
        st.subheader("📈 Visualization")
        st.line_chart(df[col])

        # Insights
        st.subheader("🧠 Smart Insights")

        max_value = df[col].max()
        min_value = df[col].min()
        avg_value = df[col].mean()

        st.write(f"🔹 Highest value: {max_value}")
        st.write(f"🔹 Lowest value: {min_value}")
        st.write(f"🔹 Average value: {round(avg_value, 2)}")

        # Trend detection
        if df[col].iloc[-1] > df[col].iloc[0]:
            st.success("📈 Overall Trend: Increasing")
        elif df[col].iloc[-1] < df[col].iloc[0]:
            st.error("📉 Overall Trend: Decreasing")
        else:
            st.info("➖ Overall Trend: Stable")

    else:
        st.warning("No numeric columns found in dataset.")

else:
    st.info("Please upload a CSV file to continue.")