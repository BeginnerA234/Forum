<h1 style="text-align: center">FORUM</h1>
<h2 style="text-align: center">О проекте</h2>



<div>Планируется форум, который будет конкурировать с социальными сетями!</div>
<div>Это то самое место, куда можно зайти после тяжелого рабочего дня =(</div>
<div>Зарегистрировать аккаунт и беседовать с людьми с разных уголков мира на абсолютно любые темы!</div>



# Что реализовано
* Регистрация пользователя
* Авторизация по двум полям - username/email
* Цитирование с сохранением id комментария - в разработке API
* ```to be continue```

### Установка
```
git clone 
cd forum/
pip install -r requirements.txt # Перед командой активировать виртуальное окружение
```
### Переменные окружения
```
Переименовать файл .env.pub -> .env
Ввести secret_key
```

### Запуск
```
python manage.py runserver
```

### Дамп БД
```
Запустить скрипт load_data.sh
#админка
username - admin
password - admin
email - admin@admin.com

Если скрипт не запустился:
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata custom_user_app.json
python manage.py loaddata forum_app.json
```

### Создание администратора
```
python manage.py createsuperuser # username и email обязателен к заполнению
```

##PS: Если был сделан дамп, команды ниже не пригодятся
### Дополнительные команды 
```
python manage.py load_country # Заполнение БД странами и флагами

python manage.py create_users # Создание пользователей

# Парсим форум и заполняем БД. Команда не рекомендуется !
python manage.py create_forum_data 

# Сносим данные из БД (custom_user, forum)
python manage.py delete_all_data
```
