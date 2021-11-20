from model.usuario_model import UsuarioModel
from service.hashes import *
from service.mensagens import *
from flask_jwt_extended import create_access_token
from datetime import timedelta

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
            usuario = cls.select().where(cls.pkcodusuario == pkcodusuario).dicts()
            if usuario:
                return msg_read_success(list(usuario))

        except Exception as error:
            return msg_read_error(error)
    
    @classmethod
    def read_usuario_update(cls, pkcodusuario):

        try:
            usuario = cls.get_or_none(cls.pkcodusuario == pkcodusuario)
            
            if usuario:
                return usuario

        except:
            return False

    @classmethod
    def read_usuario_recuperar_senha(cls, pkcodusuario):

        try:
            usuario = cls.get_or_none(cls.pkcodusuario == pkcodusuario)
            if usuario:
                return usuario
            
            return None

        except Exception as error:
            return msg_read_error(error)

    @classmethod
    def read_usuarios(cls):

        try:
            usuarios = cls.select().dicts()
            if usuarios:
                return msg_read_success(list(usuarios))
            
        except Exception as error:
            return msg_read_error(error)
    
    @classmethod
    def gera_token_recuperar_senha(cls, email, datanascimento):
        try:
            usuario = (cls.get_or_none((cls.email == email) & (cls.datanascimento == datanascimento)))
            if usuario:
                return create_access_token(identity=usuario.pkcodusuario, expires_delta=timedelta(minutes=5))

            return msg_read_error("Dados incorretos")

        except Exception as error:
            return msg_read_error(error)
    
    def update_senha_recuperar_senha(self, senha):

        try:
            self.senha = gera_senha(senha)
            self.save()
            return msg_update_success("Usuário")

        except:
            msg_update_error("Usuário")
    
    def update_usuario(self, senha, nome, telefone, email, datanascimento):

        try:
            if senha:
                self.senha = gera_senha(senha)
            
            self.nome = nome
            self.telefone = telefone
            self.email = email
            self.datanascimento = datanascimento
            self.save()

            return msg_update_success("Usuário")

        except:
            msg_update_error("Usuário")
    class Meta:
        table_name = "tbusuario"