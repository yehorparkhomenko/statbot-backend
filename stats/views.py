import datetime
import json
from dateutil import parser

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import authentication, permissions
from rest_framework.viewsets import ViewSet

from bot.models import Chat


@api_view(('GET',))
def chat_name(request: Request):
    chat_id = int(request.GET['chat_id'])
    
    chat = Chat.objects.get(id=chat_id)
    return Response(chat.title)
    

@api_view(('GET',))
def messages_by_dates(request: Request):
    chat_id = int(request.GET['chat_id'])
    startDate = request.GET['startDate']
    endDate = request.GET['endDate']

    chat = Chat.objects.get(id=chat_id)
    messages_count_stats = chat.get_messages_per_day_stats(from_date=parser.parse(startDate),
                                                           to_date=parser.parse(endDate))
    return Response(messages_count_stats)


@api_view(('GET',))
def users_by_dates(request: Request):
    chat_id = int(request.GET['chat_id'])
    startDate = request.GET['startDate']
    endDate = request.GET['endDate']
 
    chat = Chat.objects.get(id=chat_id)
    users_count_stats = chat.get_users_per_day_stats(from_date=parser.parse(startDate),
                                                           to_date=parser.parse(endDate))

    return Response(users_count_stats)


@api_view(('GET',))
def popular_words(request: Request):
    chat_id = int(request.GET['chat_id'])
    startDate = request.GET['startDate']
    endDate = request.GET['endDate']
 
    chat = Chat.objects.get(id=chat_id)
    popular_words_stats = chat.get_popular_words(from_date=parser.parse(startDate),
                                                           to_date=parser.parse(endDate))

    return Response(popular_words_stats)


@api_view(('GET',))
def most_active_users(request: Request):
    print(request.GET)
    chat_id = int(request.GET['chat_id'])
    startDate = request.GET['startDate']
    endDate = request.GET['endDate']
 
    chat = Chat.objects.get(id=chat_id)
    most_active_users_stats = chat.get_most_active_users(from_date=parser.parse(startDate),
                                                           to_date=parser.parse(endDate))

    return Response(most_active_users_stats)

