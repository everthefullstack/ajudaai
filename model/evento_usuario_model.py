from peewee import ForeignKeyField, PrimaryKeyField, SQL
from model.base_model import BaseModel
from model.evento_model import EventoModel
from model.usuario_model import UsuarioModel

class EventoUsuarioModel(BaseModel):

    pkcodeventousuario = PrimaryKeyField(primary_key=True)
    evento = ForeignKeyField(EventoModel, null=False, on_delete="NO ACTION")
    usuario = ForeignKeyField(UsuarioModel, null=False, on_delete="NO ACTION")

    class Meta:
        table_name = "tbeventousuario"
        constraints = [SQL("CONSTRAINT uk_eventousuario UNIQUE (evento_id, usuario_id)")]