## Задача
Написать сервис на Python, который имеет 3 REST ендпоинта:

* получает по HTTP имя CSV-файла (пример файла во вложении) в хранилище и суммирует каждый 10й столбец
* показывает количество задач на вычисление, которые на текущий момент в работе
* принимает ID задачи из п.1 и отображает результат в JSON-формате

Сервис должен поддерживать обработку нескольких задач от одного клиента одновременно.
Сервис должен иметь возможность горизонтально масштабироваться и загружать данные из AWS S3 и/или с локального диска.
Количество строк в csv может достигать 3*10^6.
Подключение к хранилищу может работать нестабильно.

## Решение
Для запуска данного репозитория нужно установить все зависимости из файла requirements.txt

> pip install -r requirements.txt

Если будете использовать удаленное хранилище на AWS S3 - вносим свои данные в settings.py

```bash
AWS_ACCESS_KEY_ID = None
AWS_SECRET_ACCESS_KEY = None
AWS_STORAGE_BUCKET_NAME = None
```
И конечно же:
Запустить Django

> python manage.py runserver

Запустить Celery

> celery -A drf_starttask worker -l info

P.S. Если запуск на Windows

> celery -A drf_starttask worker -l info --pool=solo

Запустить RabbitMQ

> systemctl start rabbitmq-server

P.S. Подробный гайд можете найти на офф. сайте кролика

```bash
https://www.rabbitmq.com/install-debian.html
```

и запускаем Flower т.к. это очень удобный иснтрумент для мониторинга

> celery flower --port=5566

## Заключение
Задание выполнено в соответствии с задачей и полностью и выполняет все поставленные задачи. 
При выполнении задания был использован стек: Django REST Framework (DRF) + Celery + RabbitMQ

### TODO
Сделать человеческий запуск через Docker
