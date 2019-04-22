from flask import request, abort
from flask_restplus import Resource
from rest_api.api.internal.business import create_client, update_client, delete_client
from rest_api.api.internal.serializers import client_response, client_expect
from rest_api.api.restplus import api
from rest_api.database.models import Buku, Client

ns = api.namespace('internal/client', description='API client untuk internal')

@ns.route('/')
class ClientCollection(Resource):

    @api.marshal_list_with(client_response)
    def get(self):
        """
        Menampilkan daftar client
        """
        clients = Client.query.all()
        return clients

    @api.response(201, 'Client berhasil dibuat')
    @api.expect(client_expect)
    def post(self):
        """
        Menambah client baru
        """

        data = request.json
        create_client(data)

        return None, 201

@ns.route('/<int:id>')
@api.response(404, 'Client tidak ditemukan')
class ClientItem(Resource):

    @api.response(204, "Client berhasil dihapus")
    def delete(self, id):
        """
        Menghapus client
        """
        delete_client(id)
        return None, 204
