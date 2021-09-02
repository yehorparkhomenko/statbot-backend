import aiogram
from aiogram.types.base import TelegramObject


def get_media_type(message: aiogram.types.Message):
    media_type = None
    if message.sticker:
        media_type = 'sticker'
    elif message.video:
        media_type = 'video'
    elif message.video_note:
        media_type = 'video_note'
    elif message.photo:
        media_type = 'photo'
    elif message.animation:
        media_type = 'animation'
    elif message.document:
        media_type = 'document'
    elif message.voice:
        media_type = 'voice'
    elif message.audio:
        media_type = 'audio'

    return media_type

