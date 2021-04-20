from django.db import models
from genres.models import Genre

class Movie(models.Model):
    title = models.CharField(max_length=32, verbose_name='Название фильма')
    genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Жанр фильма")
