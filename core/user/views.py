from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignUpForm
from django.contrib.auth.views import LoginView


class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = SignUpForm


class SignInView(LoginView):
    template_name = "signin.html"



