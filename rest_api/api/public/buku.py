from flask import request, abort
from flask_restplus import Resource
from rest_api.api.penerbit.serializers import book_response
from rest_api.api.restplus import api
from rest_api.database.models import Buku

ns = api.namespace('public/buku', description='API buku untuk public')

@ns.route('/')
class BukuCollection(Resource):

    @api.marshal_list_with(book_response)
    def get(self):
        """
        Menampilkan daftar buku
        """

        books = Buku.query.filter(Buku.status == "show").all()
        return books

@ns.route('/<int:id>')
class BukuItem(Resource):

    @api.marshal_with(book_response)
    def get(self, id):
        """
        Menampilkan buku berdasarkan id
        """
        buku = Buku.query.filter(Buku.id == id and Buku.status == "show").one()

        return buku
