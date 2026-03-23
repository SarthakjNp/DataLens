import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def show_basic_info(df):
    st.subheader("📊 Dataset Info")
    st.write(f"Shape: {df.shape}")

    st.subheader("Column Types")
    st.write(df.dtypes)


def show_missing_values(df):
    st.subheader("🧹 Missing Values")

    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100

    missing_df = pd.DataFrame({
        "Missing Count": missing,
        "Missing %": missing_pct
    })

    st.dataframe(missing_df)


def show_correlation(df):
    st.subheader(" Correlation Heatmap")

    numeric_df = df.select_dtypes(include=['number'])

    if numeric_df.shape[1] > 1:
        fig, ax = plt.subplots()
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Not enough numeric columns for correlation.")


def show_distributions(df):
    st.subheader(" Distribution Plots")

    col = st.selectbox("Select Column", df.columns)

    plot_type = st.selectbox("Plot Type", ["Histogram", "Box", "Count"])

    fig, ax = plt.subplots()

    if plot_type == "Histogram":
        sns.histplot(df[col].dropna(), ax=ax)

    elif plot_type == "Box":
        sns.boxplot(x=df[col], ax=ax)

    elif plot_type == "Count":
        sns.countplot(x=df[col], ax=ax)

    st.pyplot(fig)