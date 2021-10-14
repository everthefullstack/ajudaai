from model.usuario_model import UsuarioModel
from service.hashes import *
from service.mensagens import *
import json

class Usuario(UsuarioModel):

    def create_usuario(self):

        try:
            self.senha = gera_senha(self.senha)
            self.save()
            return msg_create_success("Usuário")
        
        except:
            return msg_create_error("Usuário")
    
    @classmethod
    def read_usuario(cls, pkcodusuario):

        try:

            usuario = cls.select(cls.pkcodusuario == pkcodusuario).dicts()
            if usuario:
                return msg_read_success(list(usuario))

        except Exception as error:
            return msg_read_error(error)

    @classmethod
    def read_usuarios(cls):

        try:
            usuarios = cls.select()
            if usuarios:
                return msg_read_success(json.dumps(usuarios))
            
        except Exception as error:
            return msg_read_error(error)
    
    class Meta:
        table_name = "tbusuario"