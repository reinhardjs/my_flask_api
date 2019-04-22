from flask import abort
from rest_api.database import db
from rest_api.database.models import Buku, Client
from sqlalchemy.exc import IntegrityError

def create_buku(data, account):
    isbn = data.get('isbn')
    title = data.get('title')
    pengarang = data.get('pengarang')
    penerbit = data.get('penerbit')
    harga = data.get('harga')
    status = data.get('status')

    client = Client.query.filter(Client.id == account.get("id")).one()

    buku = Buku(isbn, title, pengarang, penerbit, harga, status, client)
    db.session.add(buku)
    db.session.commit()


def update_buku(buku_id, data, account):
    buku = Post.query.filter(Buku.id == buku_id).one()

    if (buku.client_id != account.get("id")):
        abort(401, "Autentikasi tidak sesuai")

    buku.isbn = data.get('isbn')
    buku.title = data.get('title')
    buku.pengarang = data.get('pengarang')
    buku.penerbit = data.get('penerbit')
    buku.harga = data.get('harga')
    buku.status = data.get('status')
    db.session.commit()


def delete_buku(buku_id, account):
    buku = Buku.query.filter(Buku.id == buku_id).one()

    if (buku.client_id != account.get("id")):
        abort(401, "Autentikasi tidak sesuai")

    db.session.delete(buku)
    db.session.commit()
