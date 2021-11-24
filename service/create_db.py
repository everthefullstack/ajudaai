from config import string_db
from model.usuario_model import UsuarioModel
from model.evento_model import EventoModel
from model.evento_usuario_model import EventoUsuarioModel
from model.blacklist_model import BlackListModel
from service.mensagens import *

def create_db():
    
    if string_db() == True or string_db() is not None:

        print("Já existe um banco de dados, não será criado novamente.")
        return msg_create_error("Banco de dados")
        
    else:
        try:
            UsuarioModel.create_table()
            EventoModel.create_table()
            EventoUsuarioModel.create_table()
            BlackListModel.create_table()
            return msg_create_success("Banco de dados") 

        except Exception as error:
            return msg_server_error(error)