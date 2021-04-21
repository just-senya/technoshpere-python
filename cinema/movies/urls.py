from django.urls import path
from movies import views

urlpatterns = [
    path('movie/', views.movie_list, name='movie_list'),
]
