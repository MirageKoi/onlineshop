from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpRequest
from .models import PurchaseModel, ReturnModel
from .forms import PurchaseForm
from store.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

def purchaselist(request: HttpRequest):
    list = PurchaseModel.objects.filter(user=request.user)
    return render(request, "purchase_list.html", {"list":list})


def purchaseadd(request: HttpRequest, slug):
    
    if request.method == "POST":
        data = request.POST
        user = get_object_or_404(User, id=request.user.id)
        item = get_object_or_404(Product, slug=slug)
        if item.quantity >= int(data["quant"]) and request.user.coins >= item.price:
            item.quantity -= int(data["quant"]) 
            item.save()
            user.coins -= item.price * int(data["quant"])
            user.save()
            a = PurchaseModel(user=request.user, product=item, quantity=data["quant"])
            a.save()
    redirect_url = reverse_lazy("store:storelist")
    return HttpResponseRedirect(redirect_url)
    

def purchase_return(request: HttpRequest, id):
    if request.method == "POST":
        item = get_object_or_404(PurchaseModel, id=id)
        _, return_request = ReturnModel.objects.get_or_create(product_return = item)
    redirect_url = reverse_lazy("purchase:purchase_list")
    return HttpResponseRedirect(redirect_url)


def list_returns(request: HttpRequest):
    list = ReturnModel.objects.all()
    return render(request, "returns_list.html", {"list":list}) 
    

def confirm_return(request: HttpRequest, id): 
    if request.method == "POST":
        item = ReturnModel.objects.get(id=id)
        item_for_return = PurchaseModel.objects.get(id=item.product_return_id)
        restore_product = Product.objects.get(slug=item_for_return.product.slug)
        restore_product.quantity += item_for_return.quantity
        restore_product.save()
        restore_user = User.objects.get(id=item_for_return.user.id)
        restore_user.coins += item_for_return.total_cost()
        restore_user.save()
        # restore_product
        item_for_return.delete()
    redirect_url = reverse_lazy("purchase:returns_list")
    return HttpResponseRedirect(redirect_url)


