from model.evento_model import EventoModel
from model.evento_usuario_model import EventoUsuarioModel
from service.hashes import *
from service.mensagens import *

class Evento(EventoModel):

    def create_evento(self):

        try:
            self.save()
            return msg_create_success("Evento")
        
        except:
            return msg_create_error("Evento")
    
    @classmethod
    def read_evento(cls, pkcodevento):

        try:
            evento = cls.select(cls.pkcodevento == pkcodevento).dicts()
            if evento:
                return msg_read_success(list(evento))
            
        except Exception as error:
            return msg_read_error(error)

    @classmethod
    def read_eventos(cls):

        try:
            eventos = cls.select().dicts()
            if eventos:
                return msg_read_success(list(eventos))
            
        except Exception as error:
            return msg_read_error(error)
    
    @classmethod
    def read_eventos_usuario(cls, pkcodusuario):

        try:
            eventos_usuario = (cls
                                .select()
                                .join(EventoUsuarioModel, on=(cls.pkcodevento == EventoUsuarioModel.evento))
                                .where(cls.criador == pkcodusuario)
                                .dicts())

            if eventos_usuario:
                return msg_read_success(list(eventos_usuario))
            
        except Exception as error:
            return msg_read_error(error)

    class Meta:
        table_name = "tbevento"

