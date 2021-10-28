from uuid import uuid1
import os

class configuracoes():

    # Deleta todo e qualquer cache para carregar as modificações feitas no programa
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SECRET_KEY = uuid1().hex
    JWT_SECRET_KEY = uuid1().hex
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
    UPLOAD_FOLDER = "/static/img"
    URL_APP = "https://appajudaai.herokuapp.com"
    #URL_APP = "http://127.0.0.1:5000"

def string_db():
    return os.path.exists('database/ajudaai.db')