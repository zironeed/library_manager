# Django-приложение для управления книгами в библиотеке
### Реализованные эндпоинты:
#### Пользователи:
* Регистрация - users/register/
* Получение токена - users/token/
* Обновление токена - users/refresh/
#### Управление книгами:
* Создание книги - library/book/create/
* Вывод всех книг - library/book/list/
* Вывод одной книги - library/book/retrieve/<int:pk>/
* Обновление книги - library/book/update/<int:pk>/
* Удаление книги - library/book/destroy/<int:pk>/
### Настройка проекта и запуск:
1. Скопируйте репозиторий на вашу машину
2. Внесите изменения в .env файл (находится в директории library_manager)
#### Default:
1. Установите зависимости (_pip install -r requirements.txt_)
2. Перейдите в директорию library_manager (_cd .\library_manager\_)
3. Запустите celery (Unix: _celery -A config worker -l INFO_ Windows: _celery -A config worker -P eventlet -l INFO_)
4. Запустите проект (_python .\manage.py runserver_)
#### Docker:
1. Запустите Docker Engine
2. Начните сборку контейнеров (_docker-compose up -d --build_)