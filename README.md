# test_from_Nick

# Инструкция по запуску сервера DummyMessenger

## Установка зависимостей:
необходимые библиотеки:
### pip install aiohttp
### pip install asyncpg

## Настройка базы:
Создайте базу данных с именем `mydatabase`, мои пароль и username.

### CREATE USER howard WITH PASSWORD '01234'
### CREATE DATABASE mydatabase
### GRANT ALL PRIVILEGES ON DATABASE mydatabase TO howard


## Запуск сервера:
### python Server.py


## Запуск клиента для тестирования:
### python Client.py


## Пример вывода:
### Total: 8.350704431533813 seconds
### Average: 0.0016701408863067627 seconds
### Per/sec: 598.7518826698105 requests/second

