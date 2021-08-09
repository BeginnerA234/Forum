# forum


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

### Создание администратора
```
python manage.py createsuperuser # username и email обязателен к заполнению
```

### Дополнительные команды 
```
python manage.py load_country # Заполнение БД странами и флагами

python manage.py create_users # Создание пользователей

# Парсим форум и заполняем БД. Команда не рекомендуется !
python manage.py create_forum_data 
```
