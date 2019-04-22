from flask import request, abort, jsonify, make_response, session
from flask_restplus import Resource
from rest_api.api.restplus import api
from rest_api.database.models import Client

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)

ns = api.namespace("token", description="API token untuk client internal dan penerbit")

@ns.route('/claim')
class TokenClaim(Resource):

    @api.header("reset", "Isi yes untuk melakukan re-authenticate basic auth.")
    def get(self):
        auth = request.authorization

        if (request.headers.get("reset") == "yes" and not session.get("reset")):
            session["reset"] = "yes"
            return make_response('Autentikasi ulang tidak berhasil', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

        if not auth or not auth.username or not auth.password:
            return make_response('Tidak dapat diverifikasi', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})


        client = Client.query.filter(Client.username == auth.username).first()
        if not client:
            session.clear()
            return make_response('Akun tidak ditemukan dalam database', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

        if client.password == auth.password:
            jwt_identity = {
                "id" : client.id,
                "username" : client.username,
                "password" : client.password,
                "type" : client.type
            }

            session.clear()

            return {
                    "username" : client.username,
                    "client_id" : client.id,
                    "access_token" : create_access_token(identity=jwt_identity),
                    "refresh_token" : create_refresh_token(identity=jwt_identity)
                }, 200

        return make_response('Password tidak sesuai', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
