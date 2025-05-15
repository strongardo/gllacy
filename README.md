# Интернет-магазин мороженого Gllacy

Учебный проект, реализующий базовый функционал интернет-магазина на Django(только backend): от каталога товаров до корзины и личного кабинета.

## Возможности

- Регистрация, вход, выход, восстановление пароля
- Редактирование профиля пользователя
- Просмотр каталога товаров
- Поиск и фильтрация по товарам
- Добавление и удаление товаров из корзины

## Технологии

- Python 3
- Django 4
- SQLite (по умолчанию)
- HTML + Django Templates
- CSS, JS (минимально)

## Как запустить локально

```bash
git clone https://github.com/strongardo/gllacy/
cd gllacy
python -m venv venv
source venv/bin/activate  # для Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

http://127.0.0.1:8000/
