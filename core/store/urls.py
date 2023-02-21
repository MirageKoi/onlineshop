from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path("", views.StoreListView.as_view(), name="storelist"),
    path("<slug:slug>/", views.StoreDetailView.as_view(), name="detail"),
    path("create/", views.StoreCreateView.as_view(), name="create"),
    path("<slug:slug>/edit", views.StoreUpdateView.as_view(), name="update"),
]
