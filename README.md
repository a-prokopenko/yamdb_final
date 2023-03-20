[![api_yamdb workflow](https://github.com/a-prokopenko/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/a-prokopenko/yamdb_final/actions/workflows/yamdb_workflow.yml)

# YaMDb
В проекте YaMDb комплектуются отзывы (Review) пользователей на произведения (Title). Произведения делятся на категории (Category). Список категорий может быть расширен. Произведения не хранятся в базе данных проекта YaMdb. Отзывы пользователей включают в себя рейтинг, вычисляющийся путём среднего показателя общих оценок произведения.

# Ресурсы API YaMDb
**AUTH**: аутентификация.

**USERS**: пользователи.

**TITLES**: произведения.

**CATEGORIES**: категории произведений.

**GENRES**: жанры произведений.

**REVIEWS**: отзывы на произведения.

**COMMENTS**: комментарии к отзывам.

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


# Установка
1. Склонируйте репозиторий.
2. В директории `/infra/` создайте файл `.env` в котором пропишите следующие переменные окружения (для тестирования можете использовать указанные значения переменных):
 - DB_ENGINE=django.db.backends.postgresql `# указываем, что работаем с postgresql`
 - DB_NAME=postgres `# имя базы данных`
 - POSTGRES_USER=postgres `# логин для подключения к базе данных`
 - POSTGRES_PASSWORD=postgres `# пароль для подключения к БД (установите свой)`
 - DB_HOST=db `# название сервиса (контейнера)`
 - DB_PORT=5432 `# порт для подключения к БД` 
3. Находясь в папке `/infra/` выполните команду:
    ```
    docker-compose up -d --build
    ```
   Docker развернёт контейнеры, автоматически выполнит миграции, заполнит базу данных и создат superuser. 


Запущенный проект доступен по адресу [localhost](http://localhost/).
Для входа в админку ([localhost/admin](http://localhost/admin)) воспользуйтесь следующими данными:

`email: admin@bk.ru`
 `pass: admin`

Для того чтобы остановить запущенные сервисы и удалить контейнеры выполните команду: 
```
docker-compose down
```
Полная документация проекта с примерами запросов доступна по адресу [localhost/redoc](http://localhost/redoc)

Протестировать проект можно по адресу: [http://51.250.92.9/api/v1/](http://51.250.92.9/api/v1/)
