# test_from_Nick
This repo was created for the sol. of interview tasks from Nick Levashov.

# Инструкция по запуску и тестированию сервера DummyMessenger

## Установка зависимостей:
необходимые библиотеки:
### pip install aiohttp
### pip install asyncpg

## Настройка базы:
Создайте базу данных с именем `mydatabase`.

### CREATE USER howard WITH PASSWORD '01234'

### CREATE DATABASE mydatabase

### GRANT ALL PRIVILEGES ON DATABASE mydatabase TO howard
код,которого я запускал, были эти пароль и username

## Запуск сервера:
Запустите две реплики сервера:
### python Server.py

## Запуск клиента для тестирования:
### python Client.py


## После выполнения этих команд, в терминале через некоторое время будет отображен результат работы.
## Пример вывода:
### Total: 8.350704431533813 seconds
### Average: 0.0016701408863067627 seconds
### Per/sec: 598.7518826698105 requests/second

![Пример вывода:](https://drive.google.com/file/d/1ND7KnTN8Hk2FKzl8yrB0_LQxCkEeUqyV/view?usp=sharing)
