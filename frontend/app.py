# ============================================================
# 🎨 InsightNexus Streamlit Frontend (Phase 6-7 Integrated & Fixed)
# ============================================================

import streamlit as st
import requests
import pandas as pd
from io import BytesIO
import os
import socket

# ------------------------------------------------------------
# ✅ Backend URL Auto-Resolver
# ------------------------------------------------------------
# This automatically chooses correct URL based on environment
# - Local run → http://localhost:8000
# - Docker run → http://backend:8000
def get_backend_url():
    try:
        # Check if the Docker service name 'backend' is resolvable
        socket.gethostbyname("backend")
        return "http://backend:8000"
    except socket.error:
        return "http://localhost:8000"

BACKEND_URL = os.getenv("BACKEND_URL", get_backend_url())

# ------------------------------------------------------------
# Streamlit Page Configuration
# ------------------------------------------------------------
st.set_page_config(page_title="InsightNexus | AI-Powered Data Insights", layout="wide")
st.title("🚀 InsightNexus")
st.caption("Upload a CSV → Get instant EDA + AI-generated insights")

# ------------------------------------------------------------
# File Uploader
# ------------------------------------------------------------
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

def analyze_csv(file):
    """Send CSV to backend for EDA + AI insights."""
    try:
        files = {"file": (file.name, file, "text/csv")}
        response = requests.post(f"{BACKEND_URL}/eda/analyze", files=files, timeout=60)
        
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"❌ API Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Backend connection error: {e}")
        return None

# ------------------------------------------------------------
# Main Logic
# ------------------------------------------------------------
if uploaded_file is not None:
    st.info("Analyzing your dataset, please wait...")

    result = analyze_csv(uploaded_file)

    if result:
        eda_summary = result.get("eda_summary", {})
        ai_insights = result.get("ai_insights", "No AI insights available.")
        
        st.success("✅ Analysis complete!")

        # Dataset Preview
        st.subheader("📊 Data Preview")
        try:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df.head())
        except Exception as e:
            st.warning(f"⚠️ Could not preview CSV: {e}")

        # AI Insights
        st.subheader("🧠 AI Insights")
        st.info(ai_insights)

        # Expanders for Detailed EDA
        with st.expander("🔍 EDA Summary"):
            st.json(eda_summary)

        # Download Processed CSV if available
        if "processed_file" in result:
            processed_csv = BytesIO(result["processed_file"].encode())
            st.download_button(
                label="💾 Download Processed CSV",
                data=processed_csv,
                file_name="processed_dataset.csv",
                mime="text/csv"
            )
else:
    st.info("⬆️ Upload a CSV file to begin analysis.")
