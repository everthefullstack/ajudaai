from datetime import timedelta
from flask import request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from service.mensagens import *

@jwt_required
def logout():

    try:
        if request.method == "GET":

            token = get_jwt_identity()
            return msg_logout_success(create_access_token(identity=token, expires_delta=timedelta(seconds=0)))

    except Exception as error:
        
        return msg_server_error(error)

