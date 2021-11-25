from peewee import DateField, IntegerField, PrimaryKeyField, CharField, SQL
from model.base_model import BaseModel

class MetricaModel(BaseModel):

    pkcodmetrica = PrimaryKeyField(primary_key=True)
    metrica = CharField(null=False)
    qtd = IntegerField(default=0)
    data = DateField(null=False)
    
    class Meta:
        table_name = "tbmetrica"
        constraints = [SQL("CONSTRAINT uk_metrica UNIQUE (metrica, data)")]