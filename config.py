from uuid import uuid1
import os
import psycopg2

class configuracoes():

    # Deleta todo e qualquer cache para carregar as modificações feitas no programa
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SECRET_KEY = "ajudaai"
    JWT_SECRET_KEY = "ajudaai"
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
    UPLOAD_FOLDER = "/static/img"
    URL_APP = "https://appajudaai.herokuapp.com"
    #URL_APP = "http://127.0.0.1:5000"

def string_db():
    #return os.path.exists('database/ajudaai.db')
    return psycopg2.connect(host= "ec2-35-168-80-116.compute-1.amazonaws.com", 
                            port="5432", 
                            dbname="da5b7sels5sf33", 
                            user="zcweuekvmmdpsh", 
                            password="1e84a5310ec6b5e477b92c93c1399b50b76a8537f281689ac93bef4f88d8b2fc")