from django.db.models import Count
from django.test import TestCase

from custom_user.api.serializers import UserProfileSerializer
from custom_user.api.tests.setUp import SetUp
from custom_user.auth import CustomUser


class SerializerTestCase(SetUp, TestCase):

    def test_ok(self):
        queryset = CustomUser.objects.all().annotate(
            follow_count=Count('follow'),
        ).select_related('country').prefetch_related('follow', 'user_comment', 'user').order_by('id')
        data = UserProfileSerializer(queryset, many=True).data
        id_ignore_user3 = self.user_2.user.get(ignored_user=self.user_3).id
        id_ignore_user1 = self.user_2.user.get(ignored_user=self.user_1).id

        expected_data = [
            {
                'id': self.user_1.id,
                'username': 'BeginnerA234',
                'first_name': 'Kirill',
                'last_name': 'Lobashov',
                'email': 'proverka@gmail.com',
                'phone': None,
                'is_blocked': False,
                'comments_count': 3,
                'follow': [
                    {
                        'id': self.user_2.id,
                        'username': 'User2'
                    },
                    {
                        'id': self.user_3.id,
                        'username': 'User3'
                    },
                ],
                'follow_count': 2,
                'country':
                    {
                        'name': 'Россия',
                        'picture': None
                    },
                'user_ignore_list': []
            },
            {
                'id': self.user_2.id,
                'username': 'User2',
                'first_name': 'Andrey',
                'last_name': 'Palchikov',
                'email': 'palchikov_andrey@yandex.ru',
                'phone': None,
                'is_blocked': False,
                'comments_count': 1,
                'follow': [],
                'follow_count': 0,
                'country': None,
                'user_ignore_list': [
                    {
                        'id': id_ignore_user3,
                        'user': self.user_2.id,
                        'ignored_user': self.user_3.id,
                        'ignore': True
                    },
                    {
                        'id': id_ignore_user1,
                        'user': self.user_2.id,
                        'ignored_user': self.user_1.id,
                        'ignore': True
                    },
                ]
            },
            {
                'id': self.user_3.id,
                'username': 'User3',
                'first_name': 'Vladimir',
                'last_name': 'Putin',
                'email': 'VladimirVladimirovich@mail.ru',
                'phone': None,
                'is_blocked': False,
                'comments_count': 1,
                'follow': [],
                'follow_count': 0,
                'country': None,
                'user_ignore_list': []
            }
        ]
        self.assertEqual(expected_data, data)
