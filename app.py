import os
from flask import Flask, Blueprint, request, jsonify, make_response, session
from rest_api import settings

from rest_api.api.internal.endpoints.buku import ns as internal_buku_namespace
from rest_api.api.internal.endpoints.client import ns as internal_client_namespace
from rest_api.api.penerbit.endpoints.buku import ns as penerbit_buku_namespace
from rest_api.api.token.token import ns as token_namespace
from rest_api.api.public.buku import ns as public_buku_namespace

from rest_api.api.restplus import api
from rest_api.database import db, reset_database

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity
)


app = Flask(__name__)
jwt = JWTManager(app)

@app.route("/reset")
def rest():
    reset_database()
    return jsonify({
        "status" : "Reset database berhasil"
    }), 200



basedir = os.path.abspath(os.path.dirname(__file__))

def configure_app(flask_app):
    flask_app.secret_key = 'ini-adalah-super-secret-key'
    flask_app.config['SESSION_TYPE'] = 'filesystem'
    flask_app.config['JWT_SECRET_KEY'] = "ini-adalah-secretkey-jwt-asdfjkl"
    # flask_app.config['DEBUG'] = settings.FLASK_DEBUG
    # flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    # flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir  + '/rest_api', 'db.sqlite')
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(internal_client_namespace)
    api.add_namespace(internal_buku_namespace)
    api.add_namespace(penerbit_buku_namespace)
    api.add_namespace(token_namespace)
    api.add_namespace(public_buku_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)

def main():
    initialize_app(app)
    PORT = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host="0.0.0.0", port=PORT)
    # app.run()a

if __name__ == "__main__":
    main()
