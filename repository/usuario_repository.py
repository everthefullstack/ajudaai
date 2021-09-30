from model.usuario_model import UsuarioModel
from service.hashes import *
from playhouse.shortcuts import model_to_dict, dict_to_model

class Usuario(UsuarioModel):

    def create_usuario(self):

        try:
            self.senha = gera_senha(self.senha)
            self.save()
            return True
        
        except:
            return None
    
    @classmethod
    def read_usuario(cls, idusuario):

        usuario = cls.get_or_none(cls.idusuario == idusuario)
        if usuario:
            return usuario
            
        return None

    @classmethod
    def read_usuarios(cls):

        usuarios = cls.select().dicts().get()
        print(usuarios)
        if usuarios:
            return usuarios
            
        return None

    def json(self):

        return {
                'pkcodusuario': self.pkcodusuario,
                'login': self.login,
                'nome': self.nome,
                'telefone': self.telefone,
                'email': self.email,
                'idade': self.idade,
                'ativo': self.admin
               }
    
    class Meta:
        table_name = "tbusuario"