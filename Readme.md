# Дипломный проект по курсу «Django: создание функциональных веб-приложений»

API для магазина игрушек. 
API сервиса и интерфейс администрирования. 
В качестве фреймворка Django и Django REST Framework.

Описание API
-------------------

Сущности:

Игрушки
url: /toys/

Заказы
url: /orders/

Регистрация пользователя:
url: /auth/users/

Получение токена:
url: /api/auth-token/token/login/


Установка
--------------

Для загрузки репозитория выполните в консоли:
```
git clone git@github.com:Evgen-Na1movich/shop_toys_DRF.git
```
Создайте и активируйте виртуальное окужение:
```
python3 -m venv env
```
команда активации для Linux и Mac:
```
source env/bin/activate
```
Установите пакеты:
```
pip install -r requirements.txt
```
