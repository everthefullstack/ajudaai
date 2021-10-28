from random import choice
from uuid import uuid1

def gera_senha_recuperar_email():

    uuid = uuid1().hex
    nova_senha = ""

    for x in range(10):
        nova_senha = nova_senha + choice(uuid)
    
    return nova_senha