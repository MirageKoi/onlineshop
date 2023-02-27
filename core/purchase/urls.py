from django.urls import path
from . import views

app_name = "purchase"

urlpatterns = [
    path("", views.purchaselist, name="purchase_list"),
    path("<slug:slug>/add/", views.purchaseadd, name="purchase_add"),
    path("return/<int:id>", views.purchase_return, name="purchase_return"),
    path("list/", views.list_returns, name="returns_list"),
    path("list/accept/<int:id>", views.confirm_return, name="confirm_return"),
]