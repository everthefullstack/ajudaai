from model.evento_model import EventoModel
from model.evento_usuario_model import EventoUsuarioModel
from service.hashes import *
from service.mensagens import *

class EventoUsuario(EventoUsuarioModel):

    def create_evento_usuario(self):

        try:
            evento = (EventoModel
                        .select(EventoModel.pkcodevento,
                                EventoModel.criador)
                        .where((EventoModel.pkcodevento == self.evento)
                                &
                                (EventoModel.criador == self.usuario))
                        .dicts())
            print(evento)
            if evento:
                return msg_create_error("Evento Usuário")

            else:
                self.save()
                return msg_create_success("Evento Usuário")
        
        except:
            return msg_create_error("Evento Usuário")
    
    @classmethod
    def read_evento_usuario(cls, pkcodeventousuario):

        try:
            evento_usuario = cls.select(cls.pkcodeventousuario == pkcodeventousuario).dicts()
            if evento_usuario:
                return msg_read_success(list(evento_usuario))
            
        except Exception as error:
            return msg_read_error(error)

    @classmethod
    def read_eventos_usuarios(cls):

        try:
            eventos_usuarios = cls.select().dicts()
            if eventos_usuarios:
                return msg_read_success(list(eventos_usuarios))
            
        except Exception as error:
            return msg_read_error(error)
    
    class Meta:
        table_name = "tbeventousuario"