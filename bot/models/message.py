from django.db.models import *
from django.utils.timezone import now

from .user import User
from .chat import Chat


class Message(Model):
    message_id = BigIntegerField(primary_key=True)
    from_user = ForeignKey(User, on_delete=CASCADE)
    chat = ForeignKey(Chat, related_name='messages', on_delete=CASCADE)
    text = TextField(null=True)
    date_time = DateTimeField(default=now, editable=False)

