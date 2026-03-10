from django.http import HttpResponse
from django.shortcuts import render

questions = [
    {
        "id": "1",
        "text": "Столица Франции?",
        "answers": ["Париж", "Москва", "Мадрид", "Нью-Йорк"],
        "correct": "Париж"
    },
    {
        "id": "2",
        "text": "Столица России?",
        "answers": ["Санкт-Петербург", "Москва", "Мадрид", "Владивосток"],
        "correct": "Москва"

    }

]

def question(request, question_index = 0):
    current_question = questions[question_index]

    next_question_index = question_index + 1

    context = {
        "question": current_question,
        "next_question_index": next_question_index
    }

    if request.method == "POST":
        user_answer = request.POST.get("answer")
        if user_answer == current_question["correct"]:
            context["result"] = "Правильно!!!"
        else:
            context["result"] = f"Неправильно. Правильный ответ: {current_question["correct"]}"

    return render(request, "index.html", context )


