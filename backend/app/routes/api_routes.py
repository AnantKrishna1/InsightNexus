from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
import io

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Welcome to InsightNexus API — Phase 3 active 🚀"}

@router.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    # Check file extension
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")

    try:
        # Read CSV into Pandas DataFrame
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        # Generate summary
        summary = {
            "rows": len(df),
            "columns": list(df.columns),
            "numeric_summary": df.describe().to_dict()
        }

        return {"message": "CSV processed successfully!", "summary": summary}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing CSV: {str(e)}")