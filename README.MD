# InsightNexus – Full-Stack AI-Powered Data Insights Platform

InsightNexus is an **end-to-end Full Stack AI Developer project** that lets users upload datasets and instantly get **automated Exploratory Data Analysis (EDA)** along with **AI-generated insights** — all through a clean **Streamlit frontend** and **FastAPI backend**.

InsightNexus: An AI Driven Full-Stack Intelligence System

InsightNexus is a production-ready, modular ecosystem designed to unify the core disciplines of modern AI development — from data science and model orchestration to LLM-driven reasoning and end-to-end deployment. Built to demonstrate holistic proficiency across Full-Stack AI Development, Data Science, MLOps, and Agentic AI, it integrates a Streamlit-based interactive UI, a FastAPI backend, and containerized MLflow-tracked pipelines to deliver real-time exploratory data analysis and AI-generated insights.

The system bridges traditional machine learning and Generative AI by combining Pandas/NumPy-powered data pipelines, OpenAI/LLM-based reasoning layers (via LangChain), and Dockerized MLOps workflows — creating a deployable architecture that mirrors real-world enterprise AI applications. Every design decision — from RESTful API orchestration to modular containerization — reflects industry best practices for scalable, observable, and production-grade AI systems.

Rather than a random aggregation of technologies, this project demonstrates a coherent, systems-engineering approach to AI, showcasing how an engineer can architect, deploy, and manage an intelligent data-driven product that blends Data Analytics, Generative AI, LLM Ops, and Agentic reasoning into one cohesive stack.

---

## Tech Stack

| Layer | Technology |
|-------|-------------|
| Frontend | Streamlit (Python) |
| Backend | FastAPI (Python) |
| Data & ML | Pandas, Scikit-learn, NumPy, OpenAI (optional) |
| Environment | Docker + Docker Compose |
| Deployment | Local / Cloud (Render, Streamlit Cloud) |
| Version Control | Git + GitHub |

---

## Features

✅ Upload CSV files for instant EDA  
✅ AI-powered natural-language insights  
✅ Interactive data preview & statistics  
✅ Modular backend API with FastAPI  
✅ Streamlit UI with live API integration  
✅ Dockerized for easy deployment  

---

## Folder Structure

InsightNexus/
│
├── backend/
│ ├── main.py
│ ├── requirements.txt
│ └── venv/
│
├── frontend/
│ ├── app.py
│ ├── requirements.txt
│ └── venv/
│
└── docker-compose.yml


---

## Run Locally

### 1 Clone the repo
```bash
git clone https://github.com/AnantKrishna1/InsightNexus.git
cd InsightNexus

2 Backend setup

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

3️ Frontend setup

cd ../frontend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

Run with Docker

At project root:

docker-compose up --build

Deployment Options

Render → Deploy backend as a web service

Streamlit Cloud → Deploy frontend and point to backend API

AWS ECS / GCP Cloud Run → For scalable production setups

Future Enhancements

Add database (PostgreSQL / MongoDB)

Add authentication (JWT)

Enable user dashboards

Integrate LangChain for conversational analysis

Author

Akshay Singh
Full-Stack AI Developer | MLOps, LLM Ops, GenAI, Agentic AI Enthusiast

InsightNexus — because insights shouldn’t need a data scientist every time.

##  **Requirements Files**

###  `backend/requirements.txt`

```txt
fastapi
uvicorn
pandas
numpy
scikit-learn
matplotlib
seaborn
python-multipart
requests
openai
pydantic