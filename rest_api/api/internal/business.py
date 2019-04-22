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

    buku.isbn = data.get('isbn')
    buku.title = data.get('title')
    buku.pengarang = data.get('pengarang')
    buku.penerbit = data.get('penerbit')
    buku.harga = data.get('harga')
    buku.status = data.get('status')
    db.session.commit()


def delete_buku(buku_id, account):
    buku = Buku.query.filter(Buku.id == buku_id).one()

    db.session.delete(buku)
    db.session.commit()



def create_client(data):
    username = data.get('username')
    password = data.get('password')
    type = data.get('type')
    client = Client(username, password, type)

    try :
        db.session.add(client)
        db.session.commit()
    except IntegrityError:
        abort(400, "Username {} sudah digunakan".format(username))


def update_client(client_id, data):
    client = Client.query.filter(Client.id == client_id).one()
    client.username = data.get('username')
    client.password = data.get('password')
    db.session.commit()


def delete_client(client_id):
    client = Client.query.filter(Client.id == client_id).one()
    db.session.delete(client)
    db.session.commit()
