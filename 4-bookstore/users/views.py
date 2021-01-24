from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

# Create your views here.


## The following is no longer useful for django-allauth as it comes with its own user signup form.

# class SignupPageView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

