from repository.metrica_repository import Metrica
from datetime import datetime

def create_or_update_metrica(endpoint):

    try:
        metrica = Metrica(metrica = endpoint,
                          qtd = 1,
                          data = datetime.now()).create_metrica()

        if metrica == True:
            print("salvou metrica")
            return metrica

        else:
            metrica = Metrica.read_metrica(endpoint, datetime.now())
            metrica = metrica.update_metrica()
        
            if metrica == True:
                print("atualizou metrica")
                return metrica
                      
    except Exception as erro:
        print("erro " + str(erro))
        return False
    
def get_metricas():

    metricas = Metrica.read_metricas()
    return metricas