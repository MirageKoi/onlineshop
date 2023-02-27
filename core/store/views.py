from django.shortcuts import render
from django.views import View
from .models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import CreateProduct
from django.urls import reverse_lazy
from purchase.forms import PurchaseForm
from purchase.models import PurchaseModel



from django.contrib.auth.mixins import UserPassesTestMixin


class SuperUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser
    
class StoreListView(ListView):
    model = Product
    template_name = "storelist.html"


class StoreDetailView(DetailView, CreateView): 
    http_method_names = ["get", "post"]
    
    model = Product
    template_name = "storedetail.html"
    form_class = PurchaseForm

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')

    #     return render(request, self.template_name, {'form': form})




    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = PurchaseForm()
    #     return context

    # def post(self, request, *args, **kwargs):
    #     form = PurchaseForm(request.POST)
    #     if form.is_valid():
    #         product = self.get_object()
    #         quantity = form.cleaned_data['quantity']
    #         new_product = PurchaseModel.objects.create(name=product.name, description=product.description, price=product.price, quantity=quantity)
    #         return reverse_lazy("store:storelist")
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form))


class StoreCreateView(CreateView, SuperUserCheck):
    # model = Product
    form_class = CreateProduct
    template_name = "storecreate.html"
    success_url = reverse_lazy("store:storelist")


class StoreUpdateView(UpdateView, SuperUserCheck):
    model = Product
    form_class = CreateProduct
    template_name = "storecreate.html"
    success_url = reverse_lazy("store:storelist")



