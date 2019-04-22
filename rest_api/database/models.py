from datetime import datetime
from rest_api.database import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    type = db.Column(db.String(20))
    token = db.Column(db.String(300))

    def __init__(self, username, password, type):
        self.username = username
        self.password = password
        self.type = type

    def __repr__(self):
        return '<Client $r' % self.username

class Buku(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(100))
    title = db.Column(db.String(100))
    pengarang = db.Column(db.String(100))
    penerbit = db.Column(db.String(100))
    harga = db.Column(db.Integer)
    status = db.Column(db.String(10))

    client = db.relationship('Client', backref=db.backref('books', lazy='dynamic'))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)

    def __init__(self, isbn, title, pengarang, penerbit, harga, status, client):
        self.isbn = isbn
        self.title = title
        self.pengarang = pengarang
        self.penerbit = penerbit
        self.harga = harga
        self.status = status
        self.client = client

    def __repr__(self):
        return '<Buku %r' % self.title
