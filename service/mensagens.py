import json

def msg_login_error():

    return json.dumps({"msg": "Usuário não logado.", "tipo": "msg_login_error"}), 401

def msg_login_success(token):

    return json.dumps({"msg": "Usuário logado com sucesso.", "tipo": "msg_login_success","token": token}), 200

def msg_logout_success(token):

    return json.dumps({"msg": "Usuário deslogado com sucesso.", "tipo": "msg_logout_success", "token": token}), 200

def msg_server_error(error):

    return json.dumps({"msg": "Erro interno no servidor.", "tipo": "msg_server_error", "erro": f"{error}"}), 500

def msg_create_success(criado):

    return json.dumps({"msg": f"{criado} foi criado(a) com sucesso.", "tipo": "msg_create_success"}), 201

def msg_did_nothing(criado):

    return json.dumps({"msg": f"Não foram feitas alterações/inserções de {criado}.", "tipo": "msg_did_nothing"}), 202
