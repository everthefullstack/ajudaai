from peewee import  DateTimeField, ForeignKeyField, PrimaryKeyField, CharField, BooleanField
from model.base_model import BaseModel
from model.usuario_model import UsuarioModel

class EventoModel(BaseModel):

    pkcodevento = PrimaryKeyField(primary_key=True)
    titulo = CharField(null=False)
    descricao = CharField(null=False)
    localizacao = CharField(null=False)
    datahora = DateTimeField()
    inicio = DateTimeField()
    termino = DateTimeField()
    imagem = CharField()
    categoria = CharField(null=False)
    criador = ForeignKeyField(UsuarioModel, null=False, on_delete="NO ACTION")
    ativo = BooleanField(default=1)
    
    class Meta:
        table_name = "tbevento"