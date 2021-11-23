from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended.utils import decode_token
from repository.usuario_repository import Usuario
from service.gera_senhas import gera_senha_recuperar_email
from service.mensagens import *
from service.blacklist import blacklist
from service.templates import template_recuperacao_senha_1, template_recuperacao_senha_2
from service.emails import email_recuperar_senha
from config import configuracoes

def create_usuario():

    try:

        if request.method == "POST":

            usuario = Usuario(login=request.get_json()["login"],
                              senha=request.get_json()["senha"],
                              nome=request.get_json()["nome"],
                              telefone=request.get_json()["telefone"],
                              email=request.get_json()["email"],
                              datanascimento=request.get_json()["datanascimento"],
                              ativo=1).create_usuario()

            return usuario
                      
    except Exception as error:

        return msg_server_error(error)

@jwt_required()
@blacklist()
def get_usuarios():

    try:

        if request.method == "GET":

            usuarios = Usuario.read_usuario()
            return usuarios

    except Exception as error:

        return msg_server_error(error)

@jwt_required()
@blacklist()
def get_usuario():

    try:

        if request.method == "GET":

            usuario = Usuario.read_usuario(pkcodusuario=get_jwt_identity())
            return usuario

    except Exception as error:

        return msg_server_error(error)

def recuperar_senha():

    try:

        if request.method == "POST":

            token = Usuario.gera_token_recuperar_senha(request.get_json()["email"], request.get_json()["datanascimento"])
            template = template_recuperacao_senha_1()
            
            disparo = email_recuperar_senha(template=template, destinatario=request.get_json()["email"], url=configuracoes.URL_APP, token=token)
            
            if disparo:
                return msg_email_success()

            else:
                return msg_email_error()

    except Exception as error:
        return msg_server_error(error)

def trocar_senha(token):

    try:

        if request.method == "GET":

            usuario = Usuario.read_usuario_recuperar_senha(decode_token(token)["sub"])
            
            if usuario:
                
                senha = gera_senha_recuperar_email()
                usuario.update_senha_recuperar_senha(senha)
                template = template_recuperacao_senha_2()
                disparo = email_recuperar_senha(template=template, destinatario=usuario.email, senha=senha)
            
            if disparo:
                return msg_troca_senha_success()

            else:
                return msg_troca_senha_error()

    except Exception as error:
        return msg_server_error(error)

@jwt_required()
@blacklist()
def update_usuario():

    try:

        if request.method == "POST":
            
            usuario = Usuario.read_usuario_update(pkcodusuario=get_jwt_identity())
            
            usuario = usuario.update_usuario(senha=request.get_json()["senha"],
                                            nome=request.get_json()["nome"],
                                            telefone=request.get_json()["telefone"],
                                            email=request.get_json()["email"],
                                            datanascimento=request.get_json()["datanascimento"])
                                   
            return usuario
                      
    except Exception as error:

        return msg_server_error(error)