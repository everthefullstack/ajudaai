from model.usuario_model import UsuarioModel
from service.hashes import *
from service.mensagens import *

class Usuario(UsuarioModel):

    def create_usuario(self):

        try:
            self.senha = gera_senha(self.senha)
            self.save()
            return msg_create_success("Usuário")
        
        except:
            return msg_create_error("Usuário")
    
    @classmethod
    def read_usuario(cls, idusuario):

        usuario = cls.get_or_none(cls.idusuario == idusuario)
        if usuario:
            return usuario
            
        return False

    @classmethod
    def read_usuarios(cls):

        try:
            usuarios = cls.select().dicts().get()
            if usuarios:
                return msg_read_success(usuarios)
            
        except Exception as error:
            return msg_read_error(error)
    
    class Meta:
        table_name = "tbusuario"