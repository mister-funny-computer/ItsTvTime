from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    question = {
        "title": "Вопрос 1",
        "text": "Столица Франции?",
        "answers": ["Париж", "Москва", "Мадрид", "Нью-Йорк"]
    }
    return render(request, "index.html", {"question": question})


