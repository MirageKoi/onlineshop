from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView


app_name = "user"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("logout/", LogoutView.as_view(), name="logout")
]
