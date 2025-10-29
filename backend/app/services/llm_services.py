import os
import requests

CLAUDE_KEY = os.getenv("CLAUDE_API_KEY")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

def analyze_text(question, context):
    """Call an external LLM API (Claude/OpenAI) safely"""
    try:
        if CLAUDE_KEY:
            # Example: Claude via n8n proxy or direct API
            headers = {
                "Authorization": f"Bearer {CLAUDE_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "claude-3-haiku-20240307",
                "messages": [
                    {"role": "system", "content": "You are a helpful data analyst."},
                    {"role": "user", "content": f"Context: {context}\nQuestion: {question}"}
                ]
            }
            resp = requests.post("https://api.anthropic.com/v1/messages",
                                 headers=headers, json=payload)
            data = resp.json()
            return data.get("content", [{"text": "No response"}])[0]["text"]

        elif OPENAI_KEY:
            import openai
            openai.api_key = OPENAI_KEY
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a data analyst."},
                    {"role": "user", "content": f"Context: {context}\nQuestion: {question}"}
                ]
            )
            return response.choices[0].message["content"]
        else:
            return "No API key found."
    except Exception as e:
        return f"Error: {e}"
