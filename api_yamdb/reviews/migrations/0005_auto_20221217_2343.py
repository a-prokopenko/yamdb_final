# Generated by Django 3.2 on 2022-12-17 20:43

import reviews.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_user_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RemoveConstraint(
            model_name='user',
            name='username_is_not_me',
        ),
        migrations.AddField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='XXXX', max_length=255, null=True, verbose_name='код подтверждения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='биография'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('user', 'user'), ('admin', 'admin'), ('moderator', 'moderator')], default='user', max_length=20, verbose_name='роль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, null=True, unique=True, validators=[reviews.validators.validate_username]),
        ),
    ]
