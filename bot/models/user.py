from django.db.models import *


class User(Model):
    id = BigIntegerField(primary_key=True)
    first_name = TextField(null=True)
    last_name = TextField(null=True)
    username = TextField(null=True)
