from model.usuario_model import UsuarioModel
from service.hashes import *
from service.mensagens import *
from datetime import timedelta
from flask_jwt_extended import create_access_token

class Login(UsuarioModel):

    @classmethod
    def logar(cls, login, senha):
        
        try:
            usuario = cls.get_or_none(cls.login == login)
            if usuario:
                if valida_senha(senha, usuario.senha):
                    return msg_login_success(create_access_token(identity=usuario.pkcodusuario, expires_delta=timedelta(minutes=30))) 
        except:
            return msg_login_error()
    
    @classmethod
    def validar(cls, pkcodusuario, token):
        try:
            usuario = cls.get(cls.pkcodusuario == pkcodusuario)
            if usuario:
                return msg_login_success(token)

        except:
            return msg_login_error()
    class Meta:
        table_name = "tbusuario"