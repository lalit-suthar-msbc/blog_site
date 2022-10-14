from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .form import UserModel
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from .models import Account
from .models import Blog
from .models import Category
from .error_blog import find_error
from django.contrib import messages


# MESSAGE_TAGS = {
#         messages.DEBUG: 'alert-secondary',
#         messages.INFO: 'alert-info',
#         messages.SUCCESS: 'alert-success',
#         messages.WARNING: 'alert-warning',
#         messages.ERROR: 'alert-danger',
#  }


# Create your views here.
def home(request):
    if request.method == "POST":
        reg_info = UserModel(request.POST)
        print(reg_info)
        if find_error(str(reg_info.errors)):
            er=find_error(str(reg_info.errors))
            print(er)
            messages.warning(request,er)
            return redirect("/")


        if reg_info.is_valid():
            email=reg_info.cleaned_data.get("email")
            first_name=reg_info.cleaned_data.get("first_name")
            last_name=reg_info.cleaned_data.get("last_name")
            username = reg_info.cleaned_data.get('username')
            password = reg_info.cleaned_data.get('password')
            password1 = request.POST.get('password1')
            if password==password1:
                user=Account.objects.create_user(email=email,username=username,password=password)
                user.first_name=first_name
                user.last_name = last_name
                user.city="new city"
                user.save()
                messages.success(request,"User is Created successfully")
                return redirect("login")
            else:
                messages.error(request,"Password does not match")

    return render(request, "demo.html")


def login_user(request):

    if request.method == "POST":
        email = request.POST.get("email")
        ps = request.POST.get("password")
        usr = authenticate(email=email, password=ps)

        login(request, usr)
        name = request.user.username
        firstname=request.user.first_name
        print(firstname)
        blog=Blog.objects.filter(author=request.user)
        return render(request, "user_is_valid.html", {"name": name,"firstname":firstname,'blog':blog})

    return render(request, "login.html")


def log_out(request):
    logout(request)
    return HttpResponse("user is logged out")

def add_blog(request):
    if request.method =="POST":
        if request.user.is_authenticated:

            author=request.user
            print(author)
            title=request.POST.get("title")
            slug=request.POST.get("slug")
            content=request.POST.get("content")
            category = request.POST.get("category")
            Blog.objects.create(author=author,slug=slug,title=title,content=content,category=Category.objects.filter(name=category)[0])
            messages.success(request,"you blog is posted successfully")
            return redirect("add_blog")
    return render(request,'add_blog.html',{'category':Category.objects.all()})


