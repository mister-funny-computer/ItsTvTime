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
    },
    {
        "id": "3",
        "text": "Какая птица умеет летать задом наперёд?",
        "answers": ["Колибри", "Ворона", "Сокол", "Воробей"],
        "correct": "Колибри"
    },
    {
        "id": "4",
        "text": "Что есть у каждого, но никто не может это потерять?",
        "answers": ["Голова", "Пальцы", "Органы", "Тень"],
        "correct": "Тень"
    },
    {
        "id": "5",
        "text": "Какой фрукт самый вонючий?",
        "answers": ["Маракуйя", "Банан", "Дуриан", "Драконий фрукт"],
        "correct": "Дуриан"
    },
    {
        "id": "6",
        "text": "Какая нота идёт после МИ?",
        "answers": ["ДО", "ФА", "СОЛЬ", "СИ"],
        "correct": "ФА"
    },
    {
        "id": "7",
        "text": "Какой месяц самый короткий в году?",
        "answers": ["Февраль", "Январь", "Сентябрь", "Март"],
        "correct": "Февраль"
    }
]

def question(request, question_index = 0):
    current_question = questions[question_index]

    if question_index == 0:
        request.session['score'] = 0

    current_score = request.session.get('score', 0)

    next_question_index = question_index + 1

    context = {
        "question": current_question,
        "next_question_index": next_question_index,
        "score": current_score,
    }

    if request.method == "POST":
        user_answer = request.POST.get("answer")
        if user_answer == current_question["correct"]:
            context["result"] = "Правильно!!!"
            new_score = current_score + 1

            request.session['score'] = new_score
            context['score'] = new_score
        else:
            context["result"] = f"Неправильно. Правильный ответ: {current_question["correct"]}"

    return render(request, "index.html", context )

def result(request):
    final_score = request.session.get('score', 0)

    context = {
        "score": final_score,
    }
    return render(request, "result.html", context)
