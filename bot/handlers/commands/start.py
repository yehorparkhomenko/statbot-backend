from aiogram.types import Message

from ...bot import dispatcher


@dispatcher.message_handler(commands=['start'])
async def start(message: Message):
    print(message)
