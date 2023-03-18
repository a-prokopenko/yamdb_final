from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import Comment


class Command(BaseCommand):
    def handle(self, *args, **options):
        if Comment.objects.exists():
            print('Все данные в таблицу Comments уже загружены')
            return

        for row in DictReader(open('static/data/comments.csv')):
            comments = Comment(id=row['id'],
                               review_id=row['review_id'],
                               text=row['text'],
                               author_id=row['author'],
                               pub_date=row['pub_date'],
                               )
            comments.save()

        print('Данные в таблицу Comment успешно загружены')
