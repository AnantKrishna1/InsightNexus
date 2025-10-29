from app.utils.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
