# currency_converter Конвертер валют к рубрю на основе данных ЦБ РФ

Установка (локально)
Установка Docker - https://www.docker.com/
Установка Pycharm - https://www.jetbrains.com/ru-ru/pycharm/

Скачать репозиторий
Открыть проект в Pycharm
Установить python
Выбрать venv
Запустить Docker
В Pycharm выполнить установку зависимостей, запустить docker-compose.yml

Активация виртуальной среды в python (pycharm) venv:
- Открываем терминал PowerShell от админа.
- Вставляем и запускаем: Set-ExecutionPolicy RemoteSigned
- На вопрос отвечаем: A

Выполнить:
python manage.py makemigrations
python manage.py migrate
  >опционально:
  >python manage.py createsuperuser
  >ввести данные пользователя

Запуск: 
1) Открыть Docker и запустить сервер
2) В Pycharm: python manage.py runserver
