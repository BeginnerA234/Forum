from django.contrib.auth import get_user_model
from django.test import TestCase

from custom_user.models import Country, IgnoreUser
from forum.models import (
    Chapter, SubSection,
    Theme, Comment
)

User = get_user_model()


class SetUp(TestCase):

    def setUp(self):
        self.user_1 = User.objects.create(username='BeginnerA234', first_name='Kirill', last_name='Lobashov',
                                          email='proverka@gmail.com', password='proverka3004')
        self.user_2 = User.objects.create(username='User2', first_name='Andrey', last_name='Palchikov',
                                          email='palchikov_andrey@yandex.ru', password='proverka1234')
        self.user_3 = User.objects.create(username='User3', first_name='Vladimir', last_name='Putin',
                                          email='VladimirVladimirovich@mail.ru', password='proverka1234')
        chapter = Chapter.objects.create(title='Разное')
        sub_section = SubSection.objects.create(title='Таверна', chapter=chapter)
        theme = Theme.objects.create(creator=self.user_1, sub_section=sub_section, title='Вброс', comment='Random text', )
        Comment.objects.create(creator=self.user_1, theme=theme, comment='blablabla')
        Comment.objects.create(creator=self.user_1, theme=theme, comment='rqwwqr')
        Comment.objects.create(creator=self.user_1, theme=theme, comment='dfamfa')
        Comment.objects.create(creator=self.user_2, theme=theme, comment='dfamfa')
        Comment.objects.create(creator=self.user_3, theme=theme, comment='dfamfa')
        country = Country.objects.create(name='Россия')
        self.user_1.follow.add(self.user_2.id, self.user_3.id)
        User.objects.filter(pk=self.user_1.id).update(country=country)
        self.ignore_1 = IgnoreUser(user=self.user_2, ignored_user=self.user_3, ignore=True).save()
        self.ignore_2 = IgnoreUser(user=self.user_2, ignored_user=self.user_1, ignore=True).save()
