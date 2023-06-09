[![api_yamdb workflow](https://github.com/a-prokopenko/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/a-prokopenko/yamdb_final/actions/workflows/yamdb_workflow.yml)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=ffffff&color=043A6B)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=ffffff&color=043A6B)](https://www.django-rest-framework.org/)
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat&color=043A6B)](https://jwt.io/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)
# API для проекта YaMDb
YaMDb - сервис, где пользователи имеют возможность оставлять рецензии на произведения различных категорий, комментировать рецензии других пользователей, просматривать сформированные на основе оценок рейтинги произведений.

## Технологии
 - Python 3.7
 - Django 3.2
 - REST Framework 3.12.4
 - PyJWT 2.1.0
 - Gunicorn 20.0.4
 - PostgreSQL 13.0
 - Docker 23.0.1
 - Docker-compose 1.26.0
 - Nginx 1.21.3

## Системные требования
- Python 3.7
- Windows/Linux/MacOS
- Docker 23.0.1
- Docker-compose 1.26.0

# Установка и запуск
1. Установите docker:
    ```bash
    sudo apt install curl
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh  
    ```
2. Установите docker-compose:
    ```bash
    sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    ```
3. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/a-prokopenko/yamdb_final.git
    ```
3. В директории `yamdb_final/infra/` создайте файл `.env` в котором пропишите следующие переменные окружения (для тестирования можете использовать указанные значения переменных):
    ```
    SECRET_KEY=<секретный ключ проекта django>
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres # пароль для подключения к БД установите свой
    DB_HOST=db
    DB_PORT=5432
    ```
4. Находясь в директории `yamdb_final/infra/` выполните команду:

    ```
    sudo docker-compose up -d --build
    ```
   Docker развернёт контейнеры, автоматически выполнит миграции, заполнит базу данных и создат superuser. 

Запущенный проект будет доступен по адресу [localhost/api/v1/](http://localhost/api/v1/)

Для того чтобы остановить запущенные сервисы и удалить контейнеры выполните команду: 
```bash
sudo docker-compose down -v
```
 
## Для запуска на внешнем сервере с использованием функций CI/CD придерживайтесь следующего алгоритма:
1. Сделайте fork данного репозитория в ваш профиль и склонируйте его локально.
2. Войдите на ваш внешний сервер.
3. Установите Docker и docker-compose из инструкции выше.
4. Из локальной директории `yamdb_final/infra/` cкопируйте файлы `docker-compose.yml` и `nginx/default.conf` на ваш внешний сервер:
    ```bash
    scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
    scp default.conf <username>@<host>:/home/<username>/nginx/default.conf
    ```
5. Добавьте в Secrets GitHub следующие переменные окружения:

    ```
    SECRET_KEY=<секретный ключ проекта django>
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres # пароль для подключения к БД установите свой
    DB_HOST=db
    DB_PORT=5432
    
    DOCKER_PASS=<пароль от DockerHub>
    DOCKER_USER=<имя пользователя>
    
    USER=<username для подключения к серверу>
    HOST=<IP внешнего сервера>
    SSH_KEY=<ваш локальный SSH ключ (для получения команда: cat ~/.ssh/id_rsa)>
    PASSPHRASE=<пароль для SSH ключа, если он установлен>
    TELEGRAM_TO=<ID чата, в который придет сообщение>
    TELEGRAM_TOKEN=<токен вашего бота>
    ``` 

После выполнения данных инструкций, при следующем пуше в репозиторий запустится Git Actions и выполнит следующие задачи:
- выполнит проверку кода на соответствие PEP8
- произведет сборку и публикацию образа yamdb_final на ваш DockerHub
- осуществит деплой проекта на ваш внешний сервер
- отправит сообщение в ваш телеграм-бот об успешном деплое

Проект будет доступен по адресу [<ip сервера>/api/v1/](http://ip/api/v1/).

# Алгоритм регистрации пользователей
- Отправить POST-запрос с параметрами username и email на `/api/v1/auth/signup/`
- Получить письмо с кодом подтверждения на почту
- Отправить POST-запрос с параметрами username и confirmation_code на `/api/v1/auth/token/`
- Получить токен (JWT-токен)

Эти операции выполняются один раз, при регистрации пользователя. В результате пользователь получает токен и может работать с API, отправляя этот токен с каждым запросом.

# Пользовательские роли
**Аноним** — может просматривать описания произведений, читать отзывы и комментарии.

**Аутентифицированный пользователь (user)** — обладает всеми правами Анонима, может публиковать отзывы и ставить оценки произведениям, формируя рейтинг, а так же комментировать чужие отзывы и ставить им оценки.

**Модератор (moderator)** — обладает всеми правами Аутентифицированного пользователя, имеет право удалять и редактировать любые отзывы и комментарии.

**Администратор (admin)** — обладает полными правами на управление проектом и всем его содержимым.
  Для входа в админку ([localhost/admin](http://localhost/admin)) воспользуйтесь следующими данными:
  `email: admin@bk.ru`
   `pass: admin`

# Примеры запросов
Регистрация пользователя:
```
POST-запрос http://localhost/api/v1/auth/signup/:
{
"email": "string",
"username": "string"
}
Ответ:
{
"email": "string",
"username": "string"
}
```
Получение JWT-токена:
```
POST-запрос http://localhost/api/v1/auth/token/:
{
"username": "string",
"confirmation_code": "string"
}
Ответ:
{
  "token": "string"
}
```
Получение списка всех произведений:
```
GET-запрос http://localhost/api/v1/titles/:
Ответ:
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "name": "string",
      "year": 0,
      "rating": 0,
      "description": "string",
      "genre": [
        {
          "name": "string",
          "slug": "string"
        }
      ],
      "category": {
        "name": "string",
        "slug": "string"
      }
    }
  ]
}
```
Полная документация проекта с примерами запросов доступна по адресу [localhost/redoc](http://localhost/redoc)
