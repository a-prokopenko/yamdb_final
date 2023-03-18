from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import (Category, Comment, Genre, GenreTitle, Review,
                            Title, User)

MODELS_PATH = {
    'category': 'static/data/category.csv',
    'genre': 'static/data/genre.csv',
    'title': 'static/data/titles.csv',
    'genre_title': 'static/data/genre_title.csv',
    'users': 'static/data/users.csv',
    'review': 'static/data/review.csv',
    'comments': 'static/data/comments.csv',
}


class Command(BaseCommand):
    # flake8: noqa: C901
    def handle(self, *args, **options):
        for model, path in MODELS_PATH.items():
            if model == 'category':
                for row in DictReader(open(path)):
                    category = Category(id=row['id'],
                                        name=row['name'],
                                        slug=row['slug'],
                                        )
                    category.save()
            elif model == 'genre':
                for row in DictReader(open(path)):
                    genre = Genre(id=row['id'],
                                  name=row['name'],
                                  slug=row['slug'],
                                  )
                    genre.save()
            elif model == 'title':
                for row in DictReader(open(path)):
                    titles = Title(id=row['id'],
                                   name=row['name'],
                                   year=row['year'],
                                   category_id=row['category'],
                                   )
                    titles.save()
            elif model == 'genre_titles':
                for row in DictReader(open(path)):
                    genre_title = GenreTitle(id=row['id'],
                                             genre_id=row['genre_id'],
                                             title_id=row['title_id'],
                                             )
                    genre_title.save()
            elif model == 'users':
                for row in DictReader(open(path)):
                    users = User(id=row['id'],
                                 username=row['username'],
                                 email=row['email'],
                                 role=row['role'],
                                 bio=row['bio'],
                                 first_name=row['first_name'],
                                 last_name=row['last_name'],
                                 )
                    users.save()
            elif model == 'review':
                for row in DictReader(open(path)):
                    review = Review(id=row['id'],
                                    title_id=row['title_id'],
                                    text=row['text'],
                                    author_id=row['author'],
                                    score=row['score'],
                                    pub_date=row['pub_date'],
                                    )
                    review.save()
            elif model == 'comments':
                for row in DictReader(open(path)):
                    comments = Comment(id=row['id'],
                                       review_id=row['review_id'],
                                       text=row['text'],
                                       author_id=row['author'],
                                       pub_date=row['pub_date'],
                                       )
                    comments.save()
        User.objects.create_superuser('admin', 'admin@mail.ru', 'admin')
        print('Данные успешно загружены')
