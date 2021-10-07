from flask import request
from flask_jwt_extended import jwt_required
from repository.usuario_repository import Usuario
from service.mensagens import *
from service.blacklist import blacklist

def create_usuario():

    try:

        if request.method == "POST":

            usuario = Usuario(login=request.get_json()["login"],
                              senha=request.get_json()["senha"],
                              nome=request.get_json()["nome"],
                              telefone=request.get_json()["telefone"],
                              email=request.get_json()["email"],
                              idade=request.get_json()["idade"],
                              ativo=1).create_usuario()

            return usuario
                      
    except Exception as error:

        return msg_server_error(error)

@jwt_required()
@blacklist()
def get_usuarios():

    try:

        if request.method == "GET":

            usuarios = Usuario.read_usuarios()
            return usuarios

    except Exception as error:

        return msg_server_error(error)
