from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def reset_database():
    from rest_api.database.models import Buku, Client
    db.drop_all()
    db.create_all()
