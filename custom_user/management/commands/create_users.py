import random
import string

from transliterate import translit
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from custom_user.models import Country

User = get_user_model()

LETTERS_ASCII = string.ascii_lowercase

EMAIL_LIST = [
    '@mail.ru',
    '@gmail.com',
    '@yandex.ru',
]

DATA_NAME = [
    'Щербакова Виктория', 'Лопатина Екатерина', 'Королев Илья',
    'Кудрявцева Лилия', 'Попова Милана', 'Костина Виктория',
    'Акимов Мирон', 'Сафонов Макар', 'Александров Алексей',
    'Меркулов Дмитрий', 'Елизаров Сергей', 'Власов Артём',
    'Морозов Арсений', 'Короткова Анна', 'Яковлев Артемий',
    'Панфилов Елисей', 'Петров Максим', 'Савельева Айлин',
    'Жуков Максим', 'Петров Александр', 'Новиков Алексей',
    'Хохлова Агата', 'Соколов Евгений', 'Медведев Станислав',
    'Головина Варвара', 'Дмитриева Татьяна', 'Иванова Есения',
    'Макаров Максим', 'Маслов Матвей', 'Широкова Евгения',
    'Федорова Варвара', 'Антонов Сергей', 'Зайцева Василиса'
]


class Command(BaseCommand):
    help = 'Создание пользователей форума. Перед запуском выполнить команду load_country. Пароли открыты в БД'

    def handle(self, *args, **options):
        for user in DATA_NAME:
            last_name, first_name = user.split()
            username = translit(first_name + ''.join(random.choice(LETTERS_ASCII) for _ in range(random.randint(1, 3))),
                                language_code='ru', reversed=True)


            email = translit(last_name + first_name + random.choice(EMAIL_LIST),
                             language_code='ru', reversed=True)

            password = ''.join(random.choice(LETTERS_ASCII) for _ in range(random.randint(8, 10)))

            start_id = Country.objects.all().first().id
            end_id = Country.objects.all().last().id

            country = Country.objects.get(pk=random.randint(start_id, end_id))

            User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                country=country
            )
        print('Пользователи успешно создались!')