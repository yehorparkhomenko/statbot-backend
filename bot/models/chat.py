import datetime
import collections
import operator

from django.db.models import *

from ..common import utils


class Chat(Model):
    id = BigIntegerField(primary_key=True)
    first_name = TextField(null=True)
    username = TextField(null=True)
    title = TextField(null=True)
    type = TextField(null=True)

    def get_users_per_day_stats(self,
                                from_date: datetime.datetime = datetime.datetime.min,
                                to_date: datetime.datetime = datetime.datetime.now()) -> list:
        stats = list()

        datetimes = utils.range_to_list_dates(from_date, to_date)

        for i in range(0, len(datetimes)):
            date = datetimes[i]
            users = len(set(self.messages.filter(date_time__day=date.day,
                                                 date_time__month=date.month,
                                                 date_time__year=date.year).values_list('from_user_id', flat=True)))

            stats.append({
                'date': str(date.date()),
                'value': users,
                'category': 'Users count'
            })

        return stats

    def get_messages_per_day_stats(self,
                                   from_date: datetime.datetime = datetime.datetime.min,
                                   to_date: datetime.datetime = datetime.datetime.now()) -> list:
        stats = list()

        datetimes = utils.range_to_list_dates(from_date, to_date)

        for i in range(0, len(datetimes)):
            date = datetimes[i]
            try:
                messages_count = len(self.messages.filter(date_time__day=date.day,
                                                          date_time__month=date.month,
                                                          date_time__year=date.year))
                stats.append({
                    'date': str(date.date()),
                    'value': messages_count,
                    'category': 'Messages count'
                })
            except Exception as e:
                print(e)
                continue

        return stats

    def get_popular_words(self,
                          from_date: datetime.datetime = None,
                          to_date: datetime.datetime = datetime.datetime.now()) -> list:
        popular_words = dict()

        dates = utils.range_to_list_dates(from_date, to_date)

        for i in range(0, len(dates)):
            date = dates[i]
            messages = self.messages.filter(date_time__day=date.day,
                                            date_time__month=date.month,
                                            date_time__year=date.year)
            for message in messages:
                text = message.text
                words = text.split(' ')
                for word in words:
                    if not word in popular_words.keys():
                        popular_words[word] = {'word': word,
                                               'count': 1}
                    else:
                        popular_words[word]['count'] += 1

        popular_words_list = popular_words.values()
        sorted_popular_words = sorted(popular_words_list, key=lambda k: k['count'])

        return sorted_popular_words

    def get_most_active_users(self,
                              from_date: datetime.datetime = None,
                              to_date: datetime.datetime = datetime.datetime.now()) -> list:
        most_active_users = dict()

        dates = utils.range_to_list_dates(from_date, to_date)

        for i in range(0, len(dates)):
            date = dates[i]
            messages = self.messages.filter(date_time__day=date.day,
                                            date_time__month=date.month,
                                            date_time__year=date.year)

            for message in messages:
                user = message.from_user
                if user.id not in most_active_users.keys():
                    most_active_users[user.id] = {
                        'user': user.first_name,
                        'messages_count': 1,
                    }
                else:
                    most_active_users[user.id]['messages_count'] += 1

        most_active_users_list = most_active_users.values()
        sorted_active_users = sorted(most_active_users_list, key=lambda k: k['messages_count'])

        return sorted_active_users

