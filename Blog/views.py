from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .form import UserModel
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from .models import Account

# Create your views here.
def home(request):

    if request.method == "POST":

        fr = UserModel(request.POST)
        print(fr)
        if fr.is_valid():
            email=fr.cleaned_data.get("email")
            first_name=fr.cleaned_data.get("first_name")
            last_name=fr.cleaned_data.get("last_name")
            username = fr.cleaned_data.get('username')
            password = fr.cleaned_data.get('password')
            password1 = request.POST.get('password1')
            print("user is created successfully")
            user=Account.objects.create_user(email=email,username=username,password=password)
            user.save()


            # user = authenticate(username=username, password=password)

            # if request.user.is_authenticated:
            #     print(f"{request.user.username} is logged in ")
            #     print("user is logged in successfully")
    return render(request, "demo.html")


def login_user(request):
    # User_ = get_user_model()
    # data=User_.objects.all()
    # for i in data:
    #     u = User.objects.get(username=i)
    #     u.delete()

    if request.method == "POST":
        email = request.POST.get("email")
        ps = request.POST.get("password")
        usr = authenticate(email=email, password=ps)
        login(request, usr)
        name = request.user.username
        firstname=request.user.first_name
        print(firstname)
        return render(request, "user_is_valid.html", {"name": name,"firstname":firstname})
        # return HttpResponse(f"{request.user.username} is logged in")

    return render(request, "login.html")


def log_out(request):
    logout(request)
    return HttpResponse("user is logged out")
