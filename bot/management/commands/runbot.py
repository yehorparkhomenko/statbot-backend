from aiogram import executor
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Start bot'

    def handle(self, *args, **options):
        from ...bot import dispatcher
        from ... import handlers
        executor.start_polling(dispatcher)
