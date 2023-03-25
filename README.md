[![api_yamdb workflow](https://github.com/a-prokopenko/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/a-prokopenko/yamdb_final/actions/workflows/yamdb_workflow.yml)

# API для проекта YaMDb
YaMDb - сервис, где пользователи имеют возможность оставлять рецензии на произведения различных категорий, комментировать рецензии других пользователей, просматривать сформированные на основе оценок рейтинги произведений.

## Технологии
 - Python 3.7
 - Django 3.2
 - REST Framework 3.12.4
 - PyJWT 2.1.0
 - Gunicorn 20.0.4
 - PostgreSQL 12.2
 - Docker 20.10.2

## Системные требования
- Python 3.7
- Windows/Linux/MacOS

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
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres # пароль для подключения к БД установите свой
DB_HOST=db
DB_PORT=5432
```
4. Находясь в директории `yamdb_final/infra/` выполните команду:

    ```
    docker-compose up -d --build
    ```
   Docker развернёт контейнеры, автоматически выполнит миграции, заполнит базу данных и создат superuser. 

Запущенный проект доступен по адресу [localhost](http://localhost/).

Для входа в админку ([localhost/admin](http://localhost/admin)) воспользуйтесь следующими данными:
`email: admin@bk.ru`
 `pass: admin`

Для того чтобы остановить запущенные сервисы и удалить контейнеры выполните команду: 
```bash
docker-compose down -v
```



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


# Примеры запросов
Полная документация проекта с примерами запросов доступна по адресу [localhost/redoc](http://localhost/redoc)
