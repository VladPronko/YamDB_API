# API_YAMDB
## api_yamdb - это проект учебного API для сервиса отзывов к произведениям
### Авторы:
- Ilya Rogozin https://github.com/ilyarogozin
- Mia Evans https://github.com/Evansmia
- Vlad Pronko https://github.com/VladPronko
### Технологии:
- Python
- Django
- DRF

# Как запустить проект:
- Клонировать репозиторий и перейти в него:
>git clone git@github.com:ilyarogozin/api_yamdb.git

>cd api_yamdb

- Cоздать и активировать виртуальное окружение:
>python3 -m venv env

>source env/bin/activate

- Установить зависимости из файла requirements.txt:
>python3 -m pip install --upgrade pip

>pip install -r requirements.txt

- Выполнить миграции:
>python3 manage.py migrate

- Для заполнения БД sqlite тестовыми данными:
>убедитесь, что вы находитесь в корневой папке проекта(где находится manage.py)
>запустите файл csv_to_db.py из консоли: python3 csv_to_db.py

- Запустить проект:
>python3 manage.py runserver

## Примеры запросов к API можно посмотреть по запросу:
http://127.0.0.1:8000/redoc/
