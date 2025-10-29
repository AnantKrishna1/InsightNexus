# ============================================================
# 🧠 Local Dummy AI Insight Generator (Phase 4)
# ============================================================

# from openai import OpenAI
# import os
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role": "user", "content": f"Generate insights for: {eda_summary}"}]
# )
# return response.choices[0].message.content

import random

def generate_insights(eda_summary: dict) -> str:
    """
    Generate simple human-readable insights from the EDA summary.
    This is a local dummy generator – no OpenAI API used.
    """

    insights = []
    numeric_cols = list(eda_summary.get("numeric_summary", {}).keys())
    categorical_cols = list(eda_summary.get("categorical_summary", {}).keys())
    missing_values = eda_summary.get("missing_values", {})

    # 🧮 Dataset overview
    rows = eda_summary["shape"]["rows"]
    cols = eda_summary["shape"]["columns"]
    insights.append(f"The dataset has {rows} rows and {cols} columns.")

    # ⚙️ Missing values check
    total_missing = sum(missing_values.values())
    if total_missing == 0:
        insights.append("There are no missing values – the dataset is clean.")
    else:
        insights.append(f"The dataset has {total_missing} missing entries that may need handling.")

    # 📈 Numeric columns
    if numeric_cols:
        insights.append(f"Numeric columns detected: {', '.join(numeric_cols)}.")
        insights.append("Key numeric insights:")
        for col in numeric_cols:
            stats = eda_summary["numeric_summary"][col]
            mean = stats.get("mean", 0)
            std = stats.get("std", 0)
            insights.append(f" • {col} — mean {mean:.2f}, std dev {std:.2f}.")

    # 🏷️ Categorical columns
    if categorical_cols:
        insights.append(f"Categorical columns include: {', '.join(categorical_cols)}.")
        for col in categorical_cols:
            unique = eda_summary["categorical_summary"][col]["unique_count"]
            insights.append(f" • {col} has {unique} unique values.")

    # 🔗 Correlation hint
    corr = eda_summary.get("correlation_matrix", {})
    if corr and len(corr) > 1:
        insights.append("There are measurable correlations among numeric features.")

    # 🎯 Random motivational summary (to feel AI-ish)
    closing = random.choice([
        "Overall, the dataset looks ready for model training.",
        "You can proceed with feature selection or visualization.",
        "The data shows consistent quality – next step could be model experimentation."
    ])
    insights.append(closing)

    return " ".join(insights)
