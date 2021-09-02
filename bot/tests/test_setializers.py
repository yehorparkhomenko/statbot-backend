from django.conf import settings
from django.test import TestCase

from ..serializers import AsyncChatSerializer, AsyncUserSerializer, AsyncMessageSerializer


class ChatSerializerTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods")

    def setUp(self) -> None:
        print("setUp: Run once for every test method to setup clean data.")

    async def test_add_chat(self):
        """
        This tests is only for make database records for testing next features.
        :return:
        """
        chat = {
            'id': '123123',
            'first_name': 'test_user',
            'username': 'test_username',
            'title': 'test_title',
            'type': 'private',
        }

        chat_serializer = AsyncChatSerializer(data=chat)
        if await chat_serializer.is_valid_async():
            await chat_serializer.save_async()
        else:
            print(chat_serializer.errors)


