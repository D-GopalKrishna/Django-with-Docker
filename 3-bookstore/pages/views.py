from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

# class LoginView(TemplateView):
#     template_name = '/registration/login.html'

# class LogoutView(TemplateView):
#     template_name = '/registration/logout.html'



