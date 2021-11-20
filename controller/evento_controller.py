from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from repository.usuario_repository import Usuario
from repository.evento_repository import Evento
from service.mensagens import *
from service.blacklist import blacklist
from service.emails import email_edicao_evento, email_excluir_evento
from datetime import datetime

from service.templates import template_edicao_evento, template_excluir_evento

@jwt_required()
@blacklist()
def create_evento():

    try:

        if request.method == "POST":
            
            
            
            evento = Evento(titulo=request.get_json()["titulo"],
                            descricao=request.get_json()["descricao"],
                            localizacao=request.get_json()["localizacao"],
                            datahora=datetime.now().strftime("%Y-%m-%d"),
                            inicio=(datetime.strptime((request.get_json()["inicio"])[:10], "%d/%m/%Y").strftime("%Y-%m-%d")),
                            termino=(datetime.strptime((request.get_json()["termino"])[:10], "%d/%m/%Y").strftime("%Y-%m-%d")),
                            imagem=request.get_json()["imagem"],
                            categoria=request.get_json()["categoria"],
                            criador=get_jwt_identity(),
                            ativo=1).create_evento()
            return evento
                      
    except Exception as error:

        return msg_server_error(error)

@jwt_required()
@blacklist()
def get_evento():

    try:

        if request.method == "POST":

            evento = Evento.read_evento(pkcodevento=request.get_json()["pkcodevento"])
            return evento

    except Exception as error:

        return msg_server_error(error)

@jwt_required()
@blacklist()
def get_eventos():

    try:

        if request.method == "GET":

            eventos = Evento.read_eventos(pkcodusuario=get_jwt_identity())
            return eventos

    except Exception as error:

        return msg_server_error(error)

@jwt_required()
@blacklist()
def get_eventos_usuario():

    try:

        if request.method == "GET":

            eventos_usuario = Evento.read_eventos_usuario(pkcodusuario=get_jwt_identity())
            return eventos_usuario

    except Exception as error:

        return msg_server_error(error)

@jwt_required()
@blacklist()
def get_eventos_usuario_participacao():

    try:

        if request.method == "GET":

            eventos_usuario = Evento.read_eventos_usuario_participacao(pkcodusuario=get_jwt_identity())
            return eventos_usuario

    except Exception as error:

        return msg_server_error(error)

def get_eventos_publicos():

    try:

        if request.method == "GET":

            eventos = Evento.read_eventos_publicos()
            return eventos

    except Exception as error:

        return msg_server_error(error)

@jwt_required()
@blacklist()
def update_evento():

    try:

        if request.method == "POST":

            evento, valida = Evento.read_evento_update_delete(pkcodevento=request.get_json()["pkcodevento"],
                                                              pkcodusuario=get_jwt_identity())
            if valida:
                evento = evento.update_evento(titulo=request.get_json()["titulo"],
                                            descricao=request.get_json()["descricao"],
                                            localizacao=request.get_json()["localizacao"],
                                            inicio=request.get_json()["inicio"],
                                            termino=request.get_json()["termino"],
                                            categoria=request.get_json()["categoria"],
                                            imagem=request.get_json()["imagem"])

                emails_participantes = Evento.read_emails_participantes_evento(request.get_json()["pkcodevento"])

                template = template_edicao_evento()
                disparo = email_edicao_evento(template, emails_participantes, request.get_json()["titulo"])

                if evento and disparo:
                    return msg_email_update_success("Evento")

                elif evento and not disparo:
                    return evento

                else:
                    return msg_email_update_error("Evento")

            else:
                return evento

    except Exception as error:
        return msg_server_error(error)

@jwt_required()
@blacklist()
def delete_evento():

    try:

        if request.method == "POST":

            evento, valida = Evento.read_evento_update_delete(pkcodevento=request.get_json()["pkcodevento"],
                                                              pkcodusuario=get_jwt_identity())
            if valida:
                ret_evento = evento.delete_evento()
                criador = Usuario.read_usuario_update(pkcodusuario = evento.criador)
                emails_participantes = Evento.read_emails_participantes_evento(request.get_json()["pkcodevento"])
                template = template_excluir_evento()
                disparo = email_excluir_evento(template, emails_participantes, evento.titulo, 
                                               criador.nome, criador.telefone, criador.email)

                if ret_evento and disparo:
                    return msg_email_update_success("Evento")

                elif ret_evento and not disparo:
                    return ret_evento

                else:
                    return msg_email_update_error("Evento")

            else:
                return evento

    except Exception as error:

        return msg_server_error(error)