# Инструкция по запуску сервера DummyMessenger


## Установка зависимостей:
необходимые библиотеки:
### pip install aiohttp
### pip install asyncpg


## Настройка базы:
Создаем базу данных с именем `mydatabase`, мои пароль и username.
### create user howard with password '01234'
### create database mydatabase
### grant all privileges on database mydatabase to howard


## Запуск сервера:
### python Server.py


## Запуск клиента для тестирования:
### python Client.py


## Пример вывода:
### Total: 8.350704431533813 seconds
### Average: 0.0016701408863067627 seconds
### Per/sec: 598.7518826698105 requests/second

