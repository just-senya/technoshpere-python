# Generated by Django 3.2 on 2021-04-19 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('movies', '0004_auto_20210419_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(blank=True, to='genres.Genre', verbose_name='Жанр фильма'),
        ),
    ]
