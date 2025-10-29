from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def init_db():
    from app.models.user import User
    db.create_all()
