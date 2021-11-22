from flask import Flask
from controller.login_controller import login
from controller.logout_controller import logout
from controller.usuario_controller import (create_usuario, get_usuarios, recuperar_senha, trocar_senha,
                                           update_usuario)
from controller.evento_controller import (create_evento, get_eventos, get_evento, get_eventos_usuario, 
                                          get_eventos_publicos, get_eventos_usuario_participacao,
                                          update_evento, delete_evento)
from controller.evento_usuario_controller import create_evento_usuario, delete_evento_usuario
from service.create_db import create_db
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
CORS(app)
jwt = JWTManager(app)

#configurações do app
app.config.from_object("config.configuracoes")

#rotas
app.add_url_rule(rule="/login", endpoint="login", view_func=login, methods=["GET","POST"])
app.add_url_rule(rule="/logout", endpoint="logout", view_func=logout, methods=["GET"])

app.add_url_rule(rule="/usuario/create_usuario", endpoint="create_usuario", view_func=create_usuario, methods=["POST"])
app.add_url_rule(rule="/usuario/get_usuarios", endpoint="get_usuarios", view_func=get_usuarios, methods=["GET"])
app.add_url_rule(rule="/usuario/update_usuario", endpoint="update_usuario", view_func=update_usuario, methods=["POST"])

app.add_url_rule(rule="/evento/create_evento", endpoint="create_evento", view_func=create_evento, methods=["POST"])
app.add_url_rule(rule="/evento/get_eventos", endpoint="get_eventos", view_func=get_eventos, methods=["GET"])
app.add_url_rule(rule="/evento/get_evento", endpoint="get_evento", view_func=get_evento, methods=["POST"])
app.add_url_rule(rule="/evento/get_eventos_usuario", endpoint="get_eventos_usuario", view_func=get_eventos_usuario, methods=["GET"])
app.add_url_rule(rule="/evento/get_eventos_publicos", endpoint="get_eventos_publicos", view_func=get_eventos_publicos, methods=["GET"])
app.add_url_rule(rule="/evento/get_eventos_usuario_participacao", endpoint="get_eventos_usuario_participacao", view_func=get_eventos_usuario_participacao, methods=["GET"])
app.add_url_rule(rule="/evento/update_evento", endpoint="update_evento", view_func=update_evento, methods=["POST"])
app.add_url_rule(rule="/evento/delete_evento", endpoint="delete_evento", view_func=delete_evento, methods=["POST"])

app.add_url_rule(rule="/eventousuario/create_evento_usuario", endpoint="create_evento_usuario", view_func=create_evento_usuario, methods=["POST"])
app.add_url_rule(rule="/eventousuario/delete_evento_usuario", endpoint="delete_evento_usuario", view_func=delete_evento_usuario, methods=["POST"])

app.add_url_rule(rule="/recuperar_senha", endpoint="recuperar_senha", view_func=recuperar_senha, methods=["POST"])
app.add_url_rule(rule="/trocar_senha/<string:token>", endpoint="trocar_senha", view_func=trocar_senha, methods=["GET"])

"""
# inicia o servidor
if __name__ == "__main__":

    create_db()
    app.run()
"""