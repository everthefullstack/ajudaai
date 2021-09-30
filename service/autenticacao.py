from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from service.mensagens import *
from repository.login_repository import Login

def autenticar():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                
                verify_jwt_in_request()
                token = get_jwt()["sub"]
                usuario = Login.validar(token)

                if usuario:
                    return fn(*args, **kwargs) 
                    
            except Exception as error:

                return msg_login_error()

        return decorator
    return wrapper