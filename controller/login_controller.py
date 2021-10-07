from flask import request
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from repository.login_repository import Login
from service.mensagens import *
from service.blacklist import blacklist

@blacklist()
def login():

    try:

        if request.method == "POST":

            usuario = Login.logar(request.get_json()["login"], request.get_json()["senha"])
            return usuario

        elif request.method == "GET":
            
            verify_jwt_in_request()
            pkcodusuario = get_jwt_identity()
            token = request.headers["Authorization"][7::]
            usuario = Login.validar(pkcodusuario, token)
            return usuario

    except Exception as error:

        return msg_server_error(error)