from flask import Flask
from controller.login_controller import login
from controller.logout_controller import logout
from controller.usuario_controller import create_usuario, get_usuarios
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
# inicia o servidor
if __name__ == "__main__":

    create_db()
    app.run()