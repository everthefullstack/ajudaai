from model.evento_model import EventoModel
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
    
    class Meta:
        table_name = "tbevento"