from django.contrib import admin

from .models import Chat, User, Message

admin.site.register(Chat)
admin.site.register(User)
admin.site.register(Message)

