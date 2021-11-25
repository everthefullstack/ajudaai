from model.metrica_model import MetricaModel
from service.mensagens import msg_read_success, msg_read_error

class Metrica(MetricaModel):

    def create_metrica(self):

        try:
            self.save()
            return True
        
        except Exception as erro:
            print(str(erro))
            return False

    @classmethod
    def read_metricas(cls):

        try:
            metricas = cls.select().dicts()
            return msg_read_success(list(metricas))
        
        except Exception as error:
            return msg_read_error(str(error))

    @classmethod
    def read_metrica(cls, endpoint, data):

        try:
            metrica = cls.get_or_none(cls.metrica == endpoint, cls.data == data)
            return metrica
        
        except:
            return False

    def update_metrica(self):

        try:
            self.qtd = self.qtd + 1
            self.save()
            return True

        except:
            return False

    class Meta:
        table_name = "tbmetrica"