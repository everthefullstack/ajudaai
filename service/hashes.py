import bcrypt

def gera_senha(senha):
    
    return bcrypt.hashpw(senha.encode('utf8'), bcrypt.gensalt())

def valida_senha(senha, senha_hash):

    return bcrypt.checkpw(senha.encode('utf8'), senha_hash.encode("utf-8"))