from flask import request
from flask_jwt_extended import jwt_required
from repository.evento_repository import Evento
from service.mensagens import *
from service.blacklist import blacklist

@jwt_required()
@blacklist()
def create_evento():

    try:

        if request.method == "POST":

            evento = Evento(titulo=request.get_json()["titulo"],
                            descricao=request.get_json()["descricao"],
                            localizacao=request.get_json()["localizacao"],
                            datahora=request.get_json()["datahora"],
                            inicio=request.get_json()["inicio"],
                            termino=request.get_json()["termino"],
                            imagem=request.get_json()["imagem"],
                            categoria=request.get_json()["categoria"],
                            criador=request.get_json()["criador"],
                            ativo=1).create_evento()

            return evento
                      
    except Exception as error:

        return msg_server_error(error)
        