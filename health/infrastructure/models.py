from peewee import Model, AutoField, CharField, FloatField
from shared.infrastructure.database import db

class HealthRecord(Model):
    id = AutoField()
    device_id = CharField()
    bpm = FloatField()
    created_at = CharField()

    class Meta:
        database = db
        table_name = 'health_records'
