from django.urls import include, path
from rest_framework import routers

from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'chat_name', views.chat_name),
    path(r'messages_by_dates', views.messages_by_dates),
    path(r'users_by_dates', views.users_by_dates),
    path(r'most_active_users', views.most_active_users),
    path(r'popular_words', views.popular_words),
]


