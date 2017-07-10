Опросы на Django
======

Учебное приложение **polls** с официального сайта фреймворка [Django](https://djangoproject.com).
Настоятельно рекомендуется использовать для разработки не Windows, а Linux (к примеру, Ubuntu).

## Установка
* Клонируем проект с github
```bash
$ git clone git@github.com:yesnik/mysite.git
```
* Запускаем миграции базы данных
```bash
$ python manage.py migrate
```
* Запускаем сервер разработки
```bash
$ python manage.py runserver
```
* Переходим на сайт: http://127.0.0.1:8000/

* Реквизиты для [админки](http://127.0.0.1:8000/admin/): логин: *admin*, пароль: *admin*