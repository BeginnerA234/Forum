import json
import os
import shutil
from pathlib import PurePath

from django.core.management import BaseCommand

from backend import settings
from custom_user.models import Country
from parse_country import main
from django.core.files.base import File


class Command(BaseCommand):
    help = 'Наполняем базу данных странами.' \
           'В случае, если произойдет ошибка выполнить команду delete_countries' \
           'Если команда так и не выполнилась проверить parser' \
           'У пользователей windows возможны проблемы с путями!'

    def handle(self, *args, **options):

        if not os.path.exists(os.path.join(settings.BASE_DIR, 'country.json')):
            main()

        with open(os.path.join(settings.BASE_DIR, 'country.json'), 'r') as json_data:
            data = json.load(json_data)
            for country in data:
                with open(data[country]['picture'], 'rb') as img:
                    picture_path = data[country]['picture']
                    country = Country(name=data[country]['name'])
                    country.picture.save(PurePath(picture_path).parts[-1], File(img))
                    country.save()
            shutil.rmtree(os.path.join(settings.BASE_DIR, 'flags'))
            os.remove(os.path.join(settings.BASE_DIR, 'country.json'))
