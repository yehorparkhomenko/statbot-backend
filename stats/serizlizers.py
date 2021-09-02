from django.contrib.auth.models import User, Group
from rest_framework import serializers

from bot.models import Message


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class StatsSerializer(serializers.ModelSerializer):
    messages_count = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = '__all__'

    def get_messages_count(self, obj):
        print(obj)
        return obj.telegram_message_id