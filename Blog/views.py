from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .form import UserModel
from django.contrib.auth import logout


# Create your views here.
def home(request):
    if request.method == "POST":

        fr = UserModel(request.POST)
        if fr.is_valid():
            fr.save()

            print("user is saved successfully")
    return render(request, "demo.html")


def login_user(request):
    if request.method == "POST":
        name = request.POST["username"]
        ps = request.POST["password"]
        usr = authenticate(username=name, password=ps)
        login(request, usr)
        name = request.user.username
        return render(request, "user_is_valid.html", {"name": name})
        # return HttpResponse(f"{request.user.username} is logged in")

    return render(request, "login.html")


def log_out(request):
    logout(request)
    return HttpResponse("user is logged out")
