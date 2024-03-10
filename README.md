# Установка
```
cd space_mail
python -m venv venv
pip install -r ../requirements.txt
python manage.py makemigrations
```
Дополнительно необходимо поставить postgresql

Создать .env в корне репозитория со следующим содержимым:
```
login=<db_login>
password=<db_password>
database=<db_name>
```
# Запуск
```
cd space_mail
python manage.py runserver
```
```
python space_emulator.py
```
