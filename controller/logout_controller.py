from flask import request
from flask_jwt_extended import jwt_required
from repository.blacklist_repository import Blacklist
from service.mensagens import *

@jwt_required()
def logout():

    try:
        token = request.headers["Authorization"][7::]
        blacklist = Blacklist(token=token).create_blacklist()
        return blacklist

    except Exception as error:
        
        return msg_server_error(error)

