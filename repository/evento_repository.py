from model.evento_model import EventoModel
from model.evento_usuario_model import EventoUsuarioModel
from model.usuario_model import UsuarioModel
from service.hashes import *
from service.mensagens import *
from peewee import fn

class Evento(EventoModel):

    def create_evento(self):

        try:
            self.save()
            return msg_create_success("Evento")
        
        except Exception as error:
            return msg_create_error("Evento")
    
    @classmethod
    def read_evento(cls, pkcodevento):

        try:
            evento = cls.select().where(cls.pkcodevento == pkcodevento).dicts()
            return msg_read_success(list(evento))
            
        except Exception as error:
            return msg_read_error(error)

    @classmethod
    def read_eventos(cls):

        try:
            eventos = cls.select().dicts()
            return msg_read_success(list(eventos))
            
        except Exception as error:
            return msg_read_error(error)
    
    @classmethod
    def read_eventos_publicos(cls):

        try:
            eventos = (cls
                        .select()
                        .where(cls.ativo == 1)
                        .dicts())

            return msg_read_success(list(eventos))
            
        except Exception as error:
            return msg_read_error(error)
    
    #eventos que o usuario criou e seus participantes
    @classmethod
    def read_eventos_usuario(cls, pkcodusuario):

        try:
            eventos_usuario = (cls
                                .select()
                                .where(cls.criador == pkcodusuario)
                                .dicts())

            for evento_usuario in eventos_usuario:
                
                usuarios_evento = (UsuarioModel
                                    .select(UsuarioModel.nome)
                                    .join(EventoUsuarioModel, on=(EventoUsuarioModel.usuario == UsuarioModel.pkcodusuario))
                                    .where(evento_usuario["pkcodevento"] == EventoUsuarioModel.evento)
                                    .dicts())
                
                evento_usuario.update({"voluntarios": [usuario for usuario in usuarios_evento]})
                
            return msg_read_success(list(eventos_usuario))
            
        except Exception as error:
            return msg_read_error(error)
    
    #eventos que o usuario participa
    @classmethod
    def read_eventos_usuario_participacao(cls, pkcodusuario):

        try:
            
            eventos = (cls
                        .select(cls)
                        .join(EventoUsuarioModel, on=(EventoUsuarioModel.evento == cls.pkcodevento))
                        .where(EventoUsuarioModel.usuario == pkcodusuario)
                        .dicts())
            
            for evento in eventos:

                qtd_voluntarios = (EventoUsuarioModel
                                    .select(fn.COUNT(EventoUsuarioModel.pkcodeventousuario).alias("qtd"))
                                    .where(EventoUsuarioModel.evento == evento["pkcodevento"]))
                
                evento.update({"qtd_voluntarios": qtd_voluntarios.scalar()})

            return msg_read_success(list(eventos))
            
        except Exception as error:
            return msg_read_error(error)

    def update_evento(self, titulo, descricao, localizacao, 
                      inicio, termino, imagem, categoria):

        try:
            self.titulo = titulo
            self.descricao = descricao
            self.localizacao = localizacao
            self.inicio = inicio
            self.termino = termino
            self.imagem = imagem
            self.categoria = categoria
            self.save()

            return msg_update_success("Evento")

        except:
            msg_update_error("Evento")
    
    def delete_evento(self):
        
        try:
            self.ativo = 0
            self.save()
            return msg_update_success("Evento")

        except:
            msg_update_error("Evento")
    
    @classmethod
    def read_emails_participantes_evento(pkcodevento):

        try:
            
            pkcodusuarios = (EventoUsuarioModel
                                .select(EventoUsuarioModel.usuario)
                                .where(EventoUsuarioModel.evento == pkcodevento))

            emails = (UsuarioModel
                        .select(UsuarioModel.email)
                        .where(UsuarioModel.pkcodusuario._in(pkcodusuarios)))

            return emails
            
        except Exception as error:
            return msg_read_error(error)

    class Meta:
        table_name = "tbevento"

