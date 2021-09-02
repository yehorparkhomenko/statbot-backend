import datetime
import random

from django.core.management.base import BaseCommand, CommandParser

from ...models import Message, Chat, User
from ...common import utils

"""
   ,--.      <__)
   `- |________7
   .--|. \     |.\--.
  /   j \ `.7__j__\  \
 |   o   | (o)____O)  |
  \     /   J  \     /
   `---'        `---'  
art by hjw
"""

class Command(BaseCommand):
    help = 'Start bot'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('--count', type=int, default=20, required=False)
        parser.add_argument('--singlechat', default=False, action='store_true')
        parser.add_argument('--singleuser', default=False, action='store_true')

    def handle(self, *args, **options):
        database_users = User.objects.order_by('-id')
        database_chats = Chat.objects.order_by('-id')
        database_messages = Message.objects.order_by('-message_id')

        last_user_index = 0
        if len(database_users) > 0:
            last_user_index = database_users[0].id

        last_chat_index = 0
        if len(database_chats) > 0:
            last_chat_index = database_chats[0].id

        last_message_index = 0
        if len(database_messages) > 0:
            last_message_index = database_messages[0].message_id

        users = list()
        chats = list()
        messages = list()

        from_date = datetime.datetime.now() - datetime.timedelta(7)
        to_date = datetime.datetime.now()
        dates = utils.range_to_list_dates(from_date, to_date)

        count = 1 if options['singleuser'] else options['count']
        for i in range(0, count):
            entity_id = i + last_user_index + 1
            user = User(id=entity_id,
                        first_name='user' + str(entity_id),
                        username='user' + str(entity_id))
            user.save()
            users.append(user)

        count = 1 if options['singlechat'] else options['count']
        for i in range(0, count):
            entity_id = i + last_chat_index + 1
            chat = Chat(id=entity_id,
                        first_name='chat' + str(entity_id),
                        title='chat' + str(entity_id),
                        username='chat' + str(entity_id))
            chat.save()
            chats.append(chat)

        for i in range(0, options['count']):
            entity_id = i + last_message_index + 1
            date = random.choice(dates)
            user = users[0] if len(users) == 1 else users[i]
            chat = chats[0] if len(chats) == 1 else chats[i]
            message = Message(message_id=entity_id,
                              from_user=user,
                              chat=chat,
                              text='text' + str(entity_id),
                              date_time=date)
            message.save()
            messages.append(message)

        print('Added {} records'.format(options['count']))
