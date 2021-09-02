from django.test import TestCase

from ..models import Chat, User, Message


class ChatModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods")

    def setUp(self) -> None:
        print("setUp: Run once for every test method to setup clean data.")

