from peewee import Model, SqliteDatabase, PostgresqlDatabase

class BaseModel(Model):

    class Meta:
        
        #database = SqliteDatabase('database/ajudaai.db', pragmas={'foreign_keys': 1})
        database = PostgresqlDatabase(database="da5b7sels5sf33", 
                                      user="zcweuekvmmdpsh", 
                                      password="1e84a5310ec6b5e477b92c93c1399b50b76a8537f281689ac93bef4f88d8b2fc",
                                      host= "ec2-35-168-80-116.compute-1.amazonaws.com", 
                                      port=5432)