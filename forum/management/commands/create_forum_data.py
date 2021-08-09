from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from .parser import parse_forum

from forum.models import (
    Chapter, SubSection, Theme, Comment
)


User = get_user_model()


class Command(BaseCommand):
    help = 'Создание разделов, подразделов, тем и комментариев.' \
           'Запускать команду после запуска команды create_user'

    def handle(self, *args, **options):
        try:
            parse_forum.main(chapter=Chapter, subsection=SubSection, theme=Theme, comment=Comment, user=User)
            print('Форум создан')
        except:
            print('Созданы ли пользователи')
