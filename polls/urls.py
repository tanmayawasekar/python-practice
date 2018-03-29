from django.conf.urls import url

import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$',
        views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^add$', views.add_question, name='question_add'),
    url(r'^new$', views.new_question, name='question_new'),
    url(r'^delete/(?P<question_id>[0-9]+)$',
        views.delete_question, name='delete'),
    url(r'^update/(?P<question_id>[0-9]+)$',
        views.update_question, name='update'),
    # url(r'^topics/new/$',
    #     views.update_question, name='update'),
]
