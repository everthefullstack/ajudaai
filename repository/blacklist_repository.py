from service.mensagens import *
from model.blacklist_model import BlackListModel

class Blacklist(BlackListModel):

    def create_blacklist(self):

        try:
            self.save()
            return msg_logout_success(self.token)
        
        except Exception as error:
            return msg_logout_error(str(error))
    
    @classmethod
    def read_blacklist(cls, token):

        try:
            token = cls.get_or_none(cls.token == token)
            if token:
                return True
                
            return None
        
        except Exception as error:
            return msg_server_error(error)

    class Meta:
        table_name = "tbblacklist"