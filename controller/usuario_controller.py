from flask import request
from flask.json import jsonify
from repository.usuario_repository import Usuario
from service.autenticacao import autenticar
from service.mensagens import *

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
            
            if usuario:
                return msg_create_success("Usuário")
            
            else:
                return msg_did_nothing("Usuário")
                      
    except Exception as error:

        return msg_server_error(error)

@autenticar()
def get_usuarios():

    try:

        if request.method == "GET":

            usuarios = Usuario.read_usuarios()
            
            if usuarios:
                return jsonify(usuarios)

    except Exception as error:

        return msg_server_error(error)
