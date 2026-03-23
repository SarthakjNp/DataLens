import pandas as pd


def generate_insights(df):
    insights = []

    # Missing Values Insight
    for col in df.columns:
        missing_pct = df[col].isnull().mean()

        if missing_pct > 0.3:
            insights.append(f"{col} has high missing values ({round(missing_pct*100,2)}%)")

    # Numeric Analysis
    numeric_df = df.select_dtypes(include=['number'])

    for col in numeric_df.columns:
        skewness = numeric_df[col].skew()

        if abs(skewness) > 1:
            insights.append(f"{col} is highly skewed")

    # Correlation Insight
    corr = numeric_df.corr()

    for i in corr.columns:
        for j in corr.columns:
            if i != j and abs(corr.loc[i, j]) > 0.8:
                insights.append(f"{i} and {j} are strongly correlated")

    if not insights:
        insights.append("No major issues detected in dataset")

    return list(set(insights))  # remove duplicates