import pandas as pd
import json
import io

def analyze_csv(file_bytes):
    """
    Reads uploaded CSV file and performs analysis.
    Returns structured JSON with stats, columns, correlations, etc.
    """
    # Read CSV
    df = pd.read_csv(io.BytesIO(file_bytes))

    # Basic Info
    summary = {
        "shape": df.shape,
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
    }

    # Numerical summary
    numeric_summary = df.describe(include='number').to_dict()

    # Correlation matrix
    corr = df.corr(numeric_only=True).to_dict()

    # Top 5 rows (for preview)
    preview = df.head(5).to_dict(orient='records')

    result = {
        "summary": summary,
        "numeric_summary": numeric_summary,
        "correlations": corr,
        "preview": preview,
    }

    return result
