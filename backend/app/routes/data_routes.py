from flask import Blueprint, request, jsonify
import pandas as pd
from app.utils.db import db
from app.models.user import User
from app.services.llm_service import analyze_text

data_bp = Blueprint("data_bp", __name__)

@data_bp.route("/upload", methods=["POST"])
def upload_csv():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    try:
        df = pd.read_csv(file)
        preview = df.head(5).to_dict(orient="records")
        return jsonify({"preview": preview})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@data_bp.route("/ask", methods=["POST"])
def ask_ai():
    data = request.get_json()
    question = data.get("question", "")
    context = data.get("context", "")
    if not question:
        return jsonify({"error": "Question missing"}), 400
    answer = analyze_text(question, context)
    return jsonify({"answer": answer})
