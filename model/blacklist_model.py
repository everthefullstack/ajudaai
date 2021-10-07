from peewee import PrimaryKeyField, CharField
from model.base_model import BaseModel

class BlackListModel(BaseModel):

    pkcodtoken = PrimaryKeyField(primary_key=True)
    token = CharField(null=False, unique=True)
    
    class Meta:
        table_name = "tbblacklist"