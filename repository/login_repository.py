from model.usuario_model import UsuarioModel
from service.hashes import *

class Login(UsuarioModel):

    @classmethod
    def logar(cls, login, senha):
        
        try:
            usuario = cls.get_or_none(cls.login == login)
            if usuario:
                if valida_senha(senha, usuario.senha):
                    return usuario.pkcodusuario
        except:
            return None
    
    @classmethod
    def validar(cls, token):
        try:
            usuario = cls.get(cls.pkcodusuario == token)
            if usuario:
                return usuario.pkcodusuario

        except:
            return None
    
    class Meta:
        table_name = "tbusuario"