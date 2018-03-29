# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views import View
from timeit import timeit, time
from django import forms
from forms import newQuestion as form_new_question

from forms import NewQuestionTopic as FormNewQuestionTopic

from .models import Choice, Question, Topic
import datetime

from explain_helper import QuerySet as Q

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):

        search_text = self.request.GET.get('search', None)
        print(Question.objects.search_text_from_model(search_text, 'question_text'))
        if search_text:
            return Question.objects.search_text_from_model(search_text, 'question_text').order_by('-pub_date')
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
        
        

def new_question(request):
    return render(request, 'polls/questions-new.html')


def update_question(request, question_id):
    question = Question.objects.get(id=question_id)
    a = Question.objects.get(id=question_id).explain()
    print(a)
    choice = Question.objects.choice_set.all()
    return render(request, 'polls/questions-update.html',
    context = {"question":question})


def add_question(request):
    form = form_new_question(request.POST)
    if form.is_valid():
        newQuestion = Question(
            question_text = form.cleaned_data['question_text'],
            pub_date=form.cleaned_data['pub_date']
        )
        newQuestion.save()
        newQuestion.choice_set.create(choice_text=form.cleaned_data['choice1'])
        newQuestion.choice_set.create(choice_text=form.cleaned_data['choice2'])
        newQuestion.choice_set.create(choice_text=form.cleaned_data['choice3'])
        return HttpResponseRedirect(reverse('polls:question_new'))
    else:
        print(form)
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = form_new_question(initial={'pub_date': proposed_renewal_date, })

        return HttpResponseRedirect(reverse('polls:question_new'))


def delete_question(request, question_id):
    a = Question.objects.filter(id=question_id).delete()
    return HttpResponseRedirect(reverse('polls:index'))


def add_question_topic(request):
    render()

def new_question_topic(request):
    form = FormNewQuestionTopic(request.POST)
    if form.is_valid():
        t = Topic(
            topic_name = form.cleaned_data.get('topic_name', None),
            topic_type = form.cleaned_data.get('topic_type', None),
        )
        t.save()
        return HttpResponseRedirect(reverse('polls:questions_new'))
    else:
        return render()


class SearchListView(generic.base.View):

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    
    def get_queryset(self):
        search_text = self.request.GET.get('search_text', None)
        print(search_text)
        if search_text:
            return Question.objects.filter(question_text=search_text)
