from aiogram.types import Message

from ...bot import dispatcher


@dispatcher.message_handler(commands=['stats'])
async def stats(message: Message):
    pass
