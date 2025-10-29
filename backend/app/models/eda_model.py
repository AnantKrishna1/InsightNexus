# ============================================================
# InsightNexus – EDA Model
# ============================================================
import pandas as pd

def perform_eda(df: pd.DataFrame) -> dict:
    """Generate descriptive statistics and structure for CSV data."""
    try:
        summary = {
            "shape": {"rows": df.shape[0], "columns": df.shape[1]},
            "columns": list(df.columns),
            "dtypes": df.dtypes.astype(str).to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "numeric_summary": df.describe(include=[float, int]).to_dict(),
            "categorical_summary": {},
            "correlation_matrix": {},
        }

        # Categorical summaries
        for col in df.select_dtypes(include=["object", "category"]).columns:
            value_counts = df[col].value_counts().head(10).to_dict()
            summary["categorical_summary"][col] = {
                "top_values": value_counts,
                "unique_count": df[col].nunique(),
            }

        # Correlation matrix (numeric only)
        numeric_cols = df.select_dtypes(include=["number"])
        if not numeric_cols.empty:
            summary["correlation_matrix"] = numeric_cols.corr().round(3).to_dict()

        return {"status": "success", "eda_summary": summary}

    except Exception as e:
        return {"status": "error", "message": str(e)}
