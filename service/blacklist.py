from flask import request
from functools import wraps
from service.mensagens import *
from repository.blacklist_repository import Blacklist

def blacklist():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                if request.method == "GET":
                    token = request.headers["Authorization"][7::]
                    blacklist = Blacklist.read_blacklist(token)
                    if blacklist:
                        
                        return msg_login_error()
                    
                    else:
                        return fn(*args, **kwargs) 
                
                else:
                    return fn(*args, **kwargs) 
                    
            except Exception as error:

                return msg_server_error(error)

        return decorator
    return wrapper