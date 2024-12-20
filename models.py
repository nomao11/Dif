from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    min_quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    contact_info = db.Column(db.String(255), nullable=False)