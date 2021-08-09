from django.core.management import BaseCommand

from custom_user.models import Country, CustomUser
from forum.models import SubSection, Chapter


class Command(BaseCommand):
    help = 'Удаляем все записи из БД'

    def handle(self, *args, **options):
        try:
            Country.objects.all().delete()
            CustomUser.objects.all().delete()
            SubSection.objects.all().delete()
            Chapter.objects.all().delete()
            print('Все данные успешно удалилены')
        except:
            print('Произошла непредвиденная ошибка :(')
