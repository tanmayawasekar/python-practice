
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class print_request(object):

    def __init__(self, get_response):   
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_request(self, request):
        print("In Process Request ====")

    def process_view(self, request, view_func, view_args, view_kargs):
        if request.user.is_authenticated or  request.path.find('/auth/login/') != -1 or request.path.find('/auth/register') != -1:
            pass
        else:
            return HttpResponseRedirect(reverse('authenticate:login'))

class login_required(object):
    def __init__(self, get_response):
        pass
