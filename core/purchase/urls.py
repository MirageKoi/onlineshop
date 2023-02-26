from django.urls import path
from . import views

app_name = "purchase"

urlpatterns = [
    # path("<slug:slug>/purchase", views.PurchaseView.as_view(), name="purchaseone"),
    path("", views.purchaselist, name="purchase_list"),
    path("add/", views.purchaseadd, name="purchase_add")
]