from django.urls import path
from . import views

app_name = "purchase"

urlpatterns = [
    path("", views.purchaselist, name="purchase_list"),
    path("add/", views.purchaseadd, name="purchase_add"),
    path("return/<int:id>", views.purchasereturn, name="purchase_return"),
]