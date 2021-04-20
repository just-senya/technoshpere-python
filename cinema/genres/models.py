from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=32, verbose_name='Название жанра')
