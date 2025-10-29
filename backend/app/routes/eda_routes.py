# ============================================================
# 🧩 InsightNexus – EDA Routes
# ============================================================
from fastapi import APIRouter, UploadFile, File
import pandas as pd
from backend.app.models.eda_model import perform_eda
from io import StringIO

router = APIRouter()

@router.post("/analyze")
async def analyze_dataset(file: UploadFile = File(...)):
    """
    Upload a CSV and get structured EDA summary.
    """
    try:
        contents = await file.read()
        df = pd.read_csv(StringIO(contents.decode("utf-8")))
        result = perform_eda(df)
        return result
    except Exception as e:
        return {"status": "error", "message": str(e)}
