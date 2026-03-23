import streamlit as st
import pandas as pd

from utils.eda import show_basic_info, show_missing_values, show_correlation, show_distributions
from utils.insights import generate_insights
from utils.cleaning import clean_data

st.set_page_config(page_title="DataLens", layout="wide")

st.title(" DataLens — Understand Your Data Instantly")

# File Upload
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader(" Preview")
    st.dataframe(df.head())

    # Sections
    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Insights", "Visualization", "Cleaning"])

    with tab1:
        show_basic_info(df)
        show_missing_values(df)

    with tab2:
        insights = generate_insights(df)
        for ins in insights:
            st.write(f"- {ins}")

    with tab3:
        show_correlation(df)
        show_distributions(df)

    with tab4:
        df_cleaned = clean_data(df)
        st.subheader("Cleaned Data Preview")
        st.dataframe(df_cleaned.head())

        st.download_button(
            label="Download Cleaned Data",
            data=df_cleaned.to_csv(index=False),
            file_name="cleaned_data.csv",
            mime="text/csv"
        )