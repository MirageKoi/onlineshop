from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpRequest
from .models import PurchaseModel, ReturnModel
from .forms import PurchaseForm
from store.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

def purchaselist(request: HttpRequest):
    list = PurchaseModel.objects.all()
    return render(request, "purchase_list.html", {"list":list})


def purchaseadd(request: HttpRequest):
    
    if request.method == "POST":
        data = request.POST
        # form = PurchaseForm(request.POST)
        # form.cleaned_data['user'] = request.user
        
        # if form.is_valid():
        #     form.cleaned_data["user"] = request.user
        #     form.save()
        user = get_object_or_404(User, id=request.user.id)
        product = get_object_or_404(Product, title=data["title"])
        if product.quantity >= int(data["quant"]) and request.user.coins >= product.price:
            product.quantity -= int(data["quant"]) 
            product.save()
            user.coins -= product.price * int(data["quant"])
            user.save()
            a = PurchaseModel(user=request.user, title=data["title"], quantity=data["quant"])
            a.save()
        redirect_url = reverse_lazy("store:storelist")
        return HttpResponseRedirect(redirect_url)
    

def purchasereturn(request: HttpRequest, id):
    if request.method == "POST":
        item = get_object_or_404(PurchaseModel, id=id)
        _, return_request = ReturnModel.objects.get_or_create(product_return = item)
        redirect_url = reverse_lazy("purchase:purchase_list")
        return HttpResponseRedirect(redirect_url)
