from peewee import Model, SqliteDatabase

class BaseModel(Model):

    class Meta:
        
        database = SqliteDatabase('database/ajudaai.db', pragmas={'foreign_keys': 1})