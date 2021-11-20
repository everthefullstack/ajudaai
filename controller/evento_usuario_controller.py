from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from repository.evento_usuario_repository import EventoUsuario
from service.mensagens import *
from service.blacklist import blacklist

@jwt_required()
@blacklist()
def create_evento_usuario():

    try:

        if request.method == "POST":

            evento_usuario = EventoUsuario(evento=request.get_json()["pkcodevento"],
                                           usuario=get_jwt_identity()).create_evento_usuario()

            return evento_usuario
                      
    except Exception as error:

        return msg_server_error(error)

@jwt_required()
@blacklist()
def delete_evento_usuario():

    try:

        if request.method == "POST":

            evento_usuario = EventoUsuario.read_eventos_usuario_participacao(evento=request.get_json()["pkcodevento"],
                                                                             usuario=get_jwt_identity())
            
            return evento_usuario
                      
    except Exception as error:

        return msg_server_error(error)