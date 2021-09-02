import json

import aiogram

from bot.bot import dispatcher
from bot.serializers import AsyncUserSerializer, AsyncMessageSerializer, AsyncChatSerializer


@dispatcher.message_handler(lambda msg: not msg.is_command(), content_types=aiogram.types.ContentTypes.ANY)
async def on_message(message: aiogram.types.Message):
    message_json = message.as_json()
    message_dict = json.loads(message_json)
    
    message_dict['from_user'] = message_dict['from']
    message_dict['message_id'] = message_dict['message_id'] * message.chat.id

    message_serializer = AsyncMessageSerializer(data=message_dict)
    if await message_serializer.is_valid_async():
        await message_serializer.save_async()
    else:
        print(message_serializer.errors)

    print(message_json)


