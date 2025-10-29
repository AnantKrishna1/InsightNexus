# ============================================================
# 📊 EDA Route (Phase 4: Add Local AI Insights)
# ============================================================

from fastapi import APIRouter, UploadFile, File
import pandas as pd
from backend.app.services.insight_generator import generate_insights

router = APIRouter()

@router.post("/analyze")
async def analyze_csv(file: UploadFile = File(...)):
    """
    Upload CSV → Perform EDA → Generate structured summary + local AI insights
    """
    df = pd.read_csv(file.file)

    # EDA summary
    eda_summary = {
        "shape": {"rows": df.shape[0], "columns": df.shape[1]},
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "numeric_summary": df.describe().to_dict(),
        "categorical_summary": {
            col: {
                "top_values": df[col].value_counts().head(5).to_dict(),
                "unique_count": df[col].nunique()
            }
            for col in df.select_dtypes(include="object").columns
        },
        "correlation_matrix": df.corr(numeric_only=True).round(3).to_dict()
    }

    # Generate human-readable insights
    insights_text = generate_insights(eda_summary)

    return {
        "status": "success",
        "eda_summary": eda_summary,
        "ai_insights": insights_text
    }
