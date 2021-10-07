from peewee import PrimaryKeyField, CharField, BooleanField, IntegerField
from model.base_model import BaseModel

class UsuarioModel(BaseModel):

    pkcodusuario = PrimaryKeyField(primary_key=True)
    login = CharField(null=False, unique=True)
    senha = CharField(null=False)
    nome = CharField(null=False)
    telefone = CharField(null=False)
    email = CharField(null=False)
    idade = IntegerField(null=False)
    ativo = BooleanField(default=1)
    
    class Meta:
        table_name = "tbusuario"