from rest_framework import serializers
from asgiref.sync import sync_to_async

from .models import User, Chat, Message


class AsyncModelSerializer(serializers.ModelSerializer):
    @sync_to_async
    def is_valid_async(self, raise_exception=False):
        return self.is_valid(raise_exception)

    @sync_to_async
    def create_async(self, validated_data):
        return self.create(validated_data)

    @sync_to_async
    def update_async(self, instance, validated_data):
        return self.update(instance, validated_data)

    @sync_to_async
    def save_async(self, **kwargs):
        return self.save(**kwargs)


class AsyncUserSerializer(AsyncModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            'id': {'validators': []},
        }


class AsyncChatSerializer(AsyncModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

        extra_kwargs = {
            'id': {'validators': []},
        }


class AsyncMessageSerializer(AsyncModelSerializer):
    from_user = AsyncUserSerializer()
    chat = AsyncChatSerializer()

    class Meta:
        model = Message
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('from_user')
        chat_data = validated_data.pop('chat')

        user, created = User.objects.update_or_create(**user_data)
        chat, created = Chat.objects.update_or_create(**chat_data)
        message = Message.objects.create(from_user=user, chat=chat, **validated_data)

        return message


class AsyncStatSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
