from datetime import timedelta
from flask import request
from flask_jwt_extended import create_access_token, verify_jwt_in_request, get_jwt
from repository.login_repository import Login
from service.mensagens import *
from service.autenticacao import autenticar

def login():

    try:

        if request.method == "POST":

            usuario = Login.logar(request.get_json()["login"], request.get_json()["senha"])
            
            if usuario:
                return msg_login_success(create_access_token(identity=usuario, expires_delta=timedelta(minutes=60)))
            
            else:
                return msg_login_error()

        elif request.method == "GET":

            verify_jwt_in_request()
            token = get_jwt()["sub"]
            usuario = Login.validar(token)

            if usuario:
                return msg_login_success(create_access_token(identity=usuario, expires_delta=timedelta(minutes=60)))

            else:
                return msg_login_error()

    except Exception as error:

        return msg_server_error(error)