from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def movie_list(request):
    data = ["Менин атым - Кожа", "Шпион", "Мстители"]
    return HttpResponse(data)

def cinema_list(request):
    data = ["Kinopark", "Chaplin", "AsiaPark", "Cinemapark"]
    return HttpResponse(data)

def main(request):
    return render(request, 'main.html')
