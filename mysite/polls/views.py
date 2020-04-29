from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Question
from .session import auth_user_table, polls_choice_table, polls_question_table, session


def index(request):
    latest_question_list = session.query(polls_question_table).order_by(polls_question_table.c.pub_date.desc()) \
                               .all()[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = session.query(polls_question_table).filter(polls_question_table.c.id == question_id).first()
    if not question:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
