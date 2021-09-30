from config import string_db
from model.usuario_model import UsuarioModel
from service.mensagens import *

def create_db():

    if string_db() == True:

        print("Já existe um banco de dados, não será criado novamente.")
        return msg_did_nothing("Banco de dados")
        
    else:
        try:
            UsuarioModel.create_table()
            return msg_create_success("Banco de dados") 

        except Exception as error:
            
            print(f"Ocorreu um erro -> {error}")
            return msg_server_error(error)