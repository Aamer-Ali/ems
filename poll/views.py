from django.http.response import HttpResponse
from poll.models import Question
from django.http import Http404
from django.shortcuts import render


def index(request):
    context = {}
    questions = Question.objects.all()
    print(questions[0].title)
    context['title'] = 'polls'
    context['questions'] = questions
    return render(request,'polls/index.html', context)


def details(request,id = None):
    print("----------> {0}".format(id))
    context = {}
    try:
        question = Question.objects.get(id=id)
    except:
        return HttpResponse('The Question id not found in the database.')

    context['question'] = question
    return render(request,'polls/details.html', context)