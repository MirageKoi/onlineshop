from django.shortcuts import render
from django.views import View
from .models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import CreateProduct
from django.urls import reverse_lazy


from django.contrib.auth.mixins import UserPassesTestMixin


class SuperUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser
    
class StoreListView(ListView):
    model = Product
    template_name = "storelist.html"


class StoreDetailView(DetailView):
    model = Product
    template_name = "storedetail.html"


class StoreCreateView(CreateView, SuperUserCheck):
    model = Product
    form_class = CreateProduct
    template_name = "storecreate.html"
    success_url = reverse_lazy("store:store")


class StoreUpdateView(UpdateView, SuperUserCheck):
    model = Product
    form_class = CreateProduct
    template_name = "storecreate.html"
    success_url = reverse_lazy("store:store")



