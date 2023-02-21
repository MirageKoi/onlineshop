from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path("", views.StoreListView.as_view(), name="store"),
    path("create/", views.StoreCreateView.as_view(), name="create"),
    path("<slug:slug>/edit", views.StoreUpdateView.as_view(), name="update"),
]
