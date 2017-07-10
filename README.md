Опросы на Django
======

Учебное приложение **polls** с официального сайта фреймворка [Django](https://djangoproject.com).
Настоятельно рекомендуется использовать для разработки не Windows, а Linux (к примеру, Ubuntu).

## Установка
* Клонируем проект с github
```bash
$ git clone git@github.com:yesnik/mysite.git
```
* Переходим в папку с проектом и устанавливаем зависимости
```bash
$ cd mysite
$ pip install -r requirements.txt
```
* Применяем миграции
```bash
$ python manage.py migrate
```
* Создаем суперпользователя, чтобы можно было войти в админку
```bash
$ python manage.py createsuperuser
```
* Запускаем сервер разработки
```bash
$ python manage.py runserver
```
* Переходим на сайт: http://127.0.0.1:8000/

* Админка: http://127.0.0.1:8000/admin/ . Для входа используйте реквизиты созданного суперпользователя.

## Разработка

* Запустить тесты
```bash
$ python manage.py test
```
