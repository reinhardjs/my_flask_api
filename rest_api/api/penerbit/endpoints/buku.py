from flask import request, abort
from flask_restplus import Resource
from rest_api.api.penerbit.business import create_buku, update_buku, delete_buku
from rest_api.api.penerbit.serializers import book_expect, book_response
from rest_api.api.restplus import api
from rest_api.database.models import Buku

from flask_jwt_extended import (
    jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)

ns = api.namespace('penerbit/buku', description='API buku untuk penerbit')

@ns.route('/')
@api.header('Authorization', "JWT Authorization. Input: 'Bearer your-token'", required=True)
class BukuCollection(Resource):

    @api.marshal_list_with(book_response)
    @jwt_required
    def get(self):
        """
        Menampilkan daftar buku
        """

        account = get_jwt_identity()
        if (account.get("type") != "penerbit"):
            abort(401, "Autentikasi tidak sesuai")

        books = Buku.query.filter(Buku.client_id == account.get("id")).all()
        return books

    @api.response(201, 'Buku berhasil dibuat')
    @api.expect(book_expect)
    @jwt_required
    def post(self):
        """
        Menambah buku baru
        """

        account = get_jwt_identity()
        if (account.get("type") != "penerbit"):
            abort(401, "Autentikasi tidak sesuai")

        data = request.json
        create_buku(data, account)
        return None, 201

@ns.route('/<int:id>')
@api.header('Authorization', "JWT Authorization. Input: 'Bearer your-token'", required=True)
class BukuItem(Resource):
    decorators = [jwt_required]

    @api.marshal_with(book_response)
    def get(self, id):
        """
        Menampilkan buku berdasarkan id
        """

        account = get_jwt_identity()
        if (account.get("type") != "penerbit"):
            abort(401, "Autentikasi tidak sesuai")

        buku = Buku.query.filter(Buku.id == id).one()

        if (buku.client_id != account.get("id")):
            abort(401, "Autentikasi tidak sesuai")

        return buku

    @api.expect(book_expect)
    @api.response(204, "Buku berhasil diupdate")
    def put(self, id):
        """
        Mengupdate buku
        """

        account = get_jwt_identity()
        if (account.get("type") != "penerbit"):
            abort(401, "Autentikasi tidak sesuai")

        data = request.json
        update_buku(id, data, account)
        return None, 204

    @api.response(204, "Buku berhasil dihapus")
    def delete(self, id):
        """
        Menghapus buku
        """

        account = get_jwt_identity()
        if (account.get("type") != "penerbit"):
            abort(401, "Autentikasi tidak sesuai")

        delete_buku(id, account)
        return None, 204
