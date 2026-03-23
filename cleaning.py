import streamlit as st
import pandas as pd


def clean_data(df):

    df_cleaned = df.copy()

    st.subheader(" Cleaning Options")

    # Drop NA
    if st.checkbox("Drop Missing Values"):
        df_cleaned = df_cleaned.dropna()

    # Fill NA
    if st.checkbox("Fill Missing Values"):
        method = st.selectbox("Fill Method", ["Mean", "Median", "Mode"])

        for col in df_cleaned.columns:
            if df_cleaned[col].isnull().sum() > 0:

                if method == "Mean" and df_cleaned[col].dtype != 'object':
                    df_cleaned[col].fillna(df_cleaned[col].mean(), inplace=True)

                elif method == "Median" and df_cleaned[col].dtype != 'object':
                    df_cleaned[col].fillna(df_cleaned[col].median(), inplace=True)

                elif method == "Mode":
                    df_cleaned[col].fillna(df_cleaned[col].mode()[0], inplace=True)

    # Remove duplicates
    if st.checkbox("Remove Duplicates"):
        df_cleaned = df_cleaned.drop_duplicates()

    return df_cleaned