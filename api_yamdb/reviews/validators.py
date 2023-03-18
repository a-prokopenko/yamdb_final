import re
from datetime import datetime

from django.core.exceptions import ValidationError


def validate_year(value):
    if value > datetime.today().year:
        raise ValidationError('Год выпуска не может быть выше текущего!')
    return value


def validate_username(value):
    if value == 'me':
        raise ValidationError(
            'Имя пользователя недоступно.',
            params={'value': value},
        )
    if re.search(r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$', value) is None:
        raise ValidationError(
            f'Использованы недопустимые символы <{value}> в имени.',
            params={'value': value},
        )
