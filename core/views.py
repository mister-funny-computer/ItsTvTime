from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    question = {
        "title": "Вопрос 1",
        "text": "Столица Франции?",
        "answers": ["Париж", "Москва", "Мадрид", "Нью-Йорк"],
        "corect": "Париж"
    }

    context = {"question": question}

    if request.method == "POST":
        user_answer = request.POST.get("answer")
        if user_answer == question["corect"]:
            context["result"] = "Правильно!!!"
        else:
            context["result"] = f"Неправильно. Правильный ответ: {question["corect"]}"

    return render(request, "index.html", context )


