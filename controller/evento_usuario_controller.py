from flask import request
from flask_jwt_extended import jwt_required
from repository.evento_usuario_repository import EventoUsuario
from service.mensagens import *
from service.blacklist import blacklist

@jwt_required()
@blacklist()
def create_evento_usuario():

    try:

        if request.method == "POST":

            evento_usuario = EventoUsuario(evento=request.get_json()["evento"],
                                           usuario=request.headers["Authorization"][7::]).create_evento()

            return evento_usuario
                      
    except Exception as error:

        return msg_server_error(error)