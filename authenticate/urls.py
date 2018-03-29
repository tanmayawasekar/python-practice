from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView, password_reset, password_reset_done, password_change, password_change_done, PasswordChangeDoneView, PasswordChangeView

class gg(PasswordChangeDoneView):
    template_name="polls/index.html"


app_name = 'authenticate'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.loginView.as_view(), name='login'),
    url(r'^logout/$', views.logoutView.as_view(), name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^change-password/$', PasswordChangeView.as_view(), name='password_change'),
    url(r'^change-password/done$', gg.as_view(),
        name='password_change_done'),
]

