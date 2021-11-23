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

    @classmethod
    def read_eventos_usuario_participacao(cls, evento, usuario):

        try:
            evento_usuario = (cls
                                .select()
                                .where((cls.evento == evento) & (cls.usuario == usuario)))
            if evento_usuario:
                
                evento_deletado = []

                for e in evento_usuario:

                    evento_deletado.append(e)
                    return e.delete_evento_usuario()
            
            else: 
                return msg_delete_error("Evento Usuário")

        except Exception as error:
            return msg_read_error(error)

    def delete_evento_usuario(self):
        
        try:
            self.delete_instance()
            return msg_delete_success("Evento Usuário")

        except:
            msg_delete_error("Evento Usuário")
    
    class Meta:
        table_name = "tbeventousuario"