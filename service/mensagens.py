import json

def msg_login_error():
    return json.dumps({"msg": "Usuário não logado.", "tipo": "msg_login_error"}, default = str), 401

def msg_login_success(token):
    return json.dumps({"msg": "Usuário logado com sucesso.", "tipo": "msg_login_success","token": token}, default = str), 200

def msg_logout_error(token):
    return json.dumps({"msg": "Usuário não deslogado. Token válido", "tipo": "msg_logout_error", "token": token}, default = str), 202

def msg_logout_success(token):
    return json.dumps({"msg": "Usuário deslogado com sucesso. Token na Blacklist", "tipo": "msg_logout_success", "token": token}, default = str), 200

def msg_server_error(error):
    return json.dumps({"msg": "Erro interno no servidor.", "tipo": "msg_server_error", "erro": f"{error}"}, default = str), 500

def msg_create_success(criado):
    return json.dumps({"msg": f"{criado} foi criado(a) com sucesso.", "tipo": "msg_create_success"}, default = str), 201

def msg_create_error(criado):
    return json.dumps({"msg": f"Não foram feitas alterações/inserções de {criado}.", "tipo": "msg_create_error"}, default = str), 202

def msg_update_success(alterado):
    return json.dumps({"msg": f"{alterado} foi alterado(a) com sucesso.", "tipo": "msg_update_success"}, default = str), 201

def msg_update_error(alterado):
    return json.dumps({"msg": f"Não foram feitas alterações de {alterado}.", "tipo": "msg_update_error"}, default = str), 202

def msg_read_success(lista):
    return json.dumps({"msg": "Foi realizada a consulta.", "tipo": "msg_read_success", "consulta": lista}, default = str), 200

def msg_read_error(error):
    return json.dumps({"msg": "Não foi possível realizar a consulta.", "tipo": "msg_read_error", "erro": f"{error}"}, default = str), 202

def msg_email_success():
    return json.dumps({"msg": "Foi enviado o email.", "tipo": "msg_email_success"}, default = str), 200

def msg_email_error():
    return json.dumps({"msg": "Não foi possível enviar o email.", "tipo": "msg_email_error"}, default = str), 202

def msg_email_update_success(alterado):
    return json.dumps({"msg": f"Foi feita a alteração no {alterado} e seus participantes foram notificados.", "tipo": "msg_email_update_success"}, default = str), 200

def msg_email_update_error(alterado):
    return json.dumps({"msg": f"Não foi possível alterar o {alterado}. e nenhum participante foi notificado.", "tipo": "msg_email_update_error"}, default = str), 202
 
def msg_troca_senha_success():
    return json.dumps({"msg": "Foi enviada uma nova senha para o seu email.", "tipo": "msg_troca_senha_success"}, default = str), 200

def msg_troca_senha_error():
    return json.dumps({"msg": "Não Foi enviada uma nova senha para o seu email, refaça o processo ou consulte um administrador", "tipo": "msg_troca_senha_error"}, default = str), 202

def msg_delete_error(deletado):
    return json.dumps({"msg": f"{deletado} nao deletado.", "tipo": "msg_delete_error"}, default = str), 202

def msg_delete_success(deletado):
    return json.dumps({"msg": f"{deletado} deletado com sucesso.", "tipo": "msg_delete_success"}, default = str), 200
