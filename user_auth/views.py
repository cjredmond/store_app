from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from user_auth.models import Cart

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    def get_success_url(self):
        return reverse('login')

class CartDetailView(DetailView):
    model = Cart

class CartDestroyView()
