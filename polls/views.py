# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
import datetime

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        print(request.POST)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def new_question(request):
    return render(request, 'polls/questions-new.html')


def add_question(request):
    question_text = request.POST['question_text']
    pub_date = request.POST['pub_date']
    choice_text = request.POST['choice']
    newQuestion = Question(
        question_text = question_text,
        pub_date=datetime.datetime.strptime(pub_date, "%Y-%m-%d").date()
    )
    newQuestion.save()
    # newChoice = Choice(question=newQuestion, choice_text = choice_text)
    # newChoice.save()
    newQuestion.choice_set.create(choice_text = choice_text)
    return HttpResponseRedirect(reverse('polls:question_new'))
