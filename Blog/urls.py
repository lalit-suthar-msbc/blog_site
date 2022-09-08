from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="blog"),
    path("login/",views.login_user,name="login"),
    path("log_out/", views.log_out, name="login")
]

