# ============================================================
#  InsightNexus Backend (Main FastAPI App)
# ============================================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# ============================================================
#  Load Environment Variables
# ============================================================
load_dotenv()

# ============================================================
#  FastAPI App Initialization
# ============================================================
app = FastAPI(
    title="InsightNexus Backend API",
    description="Agentic AI + MLOps project backend (Phase 4 — EDA + Data Insights)",
    version="4.0.0"
)

# ============================================================
#  CORS Configuration
# ============================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ✅ Allow all during development (restrict later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
#  Import and Include Routers
# ============================================================
from backend.app.routes import api_routes, eda_routes  # ✅ Added eda_routes for Phase 4

# Register routers
app.include_router(api_routes.router, prefix="/api", tags=["CSV & API"])
app.include_router(eda_routes.router, prefix="/eda", tags=["EDA & Analysis"])

# ============================================================
#  Root Endpoint
# ============================================================
@app.get("/")
def root():
    return {
        "message": "🚀 InsightNexus Backend is Live (Phase 4: EDA + Data Insights)",
        "version": "4.0.0",
        "status": "healthy"
    }

# ============================================================
#  Health Check Endpoint
# ============================================================
@app.get("/health")
def health_check():
    return {"status": "✅ Server healthy and ready for EDA operations"}

# ============================================================
#  Run (for local testing)
# ============================================================
# Run from project root using:
#   uvicorn backend.app.main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=8000, reload=True)
