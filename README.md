# praktikum_new_diplom
***
![foodgram-workflow](https://github.com/olegvpc/foodgram-project-react/workflows/foodgram-workflow/badge.svg)
***
## Дипломный проект курса Python-разработчик Яндекс-Практикум
***
### Описание:
С помощью сервиса Foodgram - продуктовый помощник, пользователи смогут публиковать рецепты, 
подписываться на других пользователей, фильтровать рецепты по тегам,
добавлять понравившиеся рецепты в список "Избранное" 
и скачивать список продуктов из "Избранное" в файл.
***
### Проект доступен по ссылке:

http://62.84.112.83
#### ssh diplom@62.84.112.83 вход через терминал


### Стек технологий
```
Python 3
Django
Django REST Framework
Djoser
Docker
```
## Как запустить:
Скачать проект по адресу:
https://github.com/olegvpc/foodgram-project-react.git

### Установка
1. Установка docker и docker-compose
Инструкция по установке доступна в официальной инструкции

2. Создать файл .env с переменными окружения
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres # Имя базы данных
POSTGRES_USER=postgres # Администратор базы данных
POSTGRES_PASSWORD=postgres # Пароль администратора
DB_HOST=db
DB_PORT=5432
SECRET_KEY=SECRET_KEY - секретный ключ шифрования Django
```
3. Сборка и запуск контейнера
```docker-compose up -d --build```
4. Миграции

```docker-compose exec backend python manage.py makemigrations```

```docker-compose exec backend python manage.py migrate```
5. Сбор статики

```docker-compose exec backend python manage.py collectstatic --no input```
6. Создание суперпользователя Django

```docker-compose exec backend python manage.py createsuperuser```
7. Копирование данных с ингридиентами из файла

```docker-compose exec backend python manage.py add_ingredients```

8. Копирование данных с тэгами из файла

```docker-compose exec backend python manage.py add_tag```

Автор проекта: Ткач Олег
