from django.conf.urls import url

import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$',
        views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^question/new$', views.new_question, name='question_new'),
    url(r'^question/add$', views.add_question, name='question_add'),
    # url(r'^choice/new$', views.new_choice, name='choice_new'),
    # url(r'^choice/add$', views.add_choice, name='choice_add'),
]
