# EffectiveAcademy Labs

Репозиторий содержит проект библиотеки, написанной на Django в рамках пособия с сайта: https://developer.mozilla.org/ru/docs/Learn/Server-side/Django

### Необходимые инструменты
- Python: 3.12+
- Poetry 1.8.3


### Для запуска проекта необходимо:
- клонировать репозиторий
  ```
  git clone https://github.com/kiokroel/EffectiveAcademyBackendLabs.git
  ```
- установить poetry любым удобным способом:
  [документация](https://python-poetry.org/docs/)
- установить зависимости 
  ```
  poetry install
  ```
 - создать в корне проекта файл .env и указать в нем поля
  ```
  SECRET_KEY=..
  DEBUG=<True or False>
  ```
- прогнать миграции базы данных
  ```
  poetry run python manage.py makemigrations 
  ```
- запустить сервер
  ```
  python manage.py runserver
  ```
