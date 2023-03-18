from csv import DictReader

from django.core.management import BaseCommand

from reviews.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.exists():
            print('Все данные в таблицу User уже загружены')
            return

        for row in DictReader(open('static/data/users.csv')):
            user = User(id=row['id'],
                        username=row['username'],
                        email=row['email'],
                        role=row['role'],
                        bio=row['bio'],
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        )
            user.save()

        print('Данные в таблицу User успешно загружены')
