from .models import Account
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.forms import forms


class UserModel(ModelForm):
    class Meta:
        model = Account
        fields = ["first_name", "last_name", "email", "username", "password"]

# class UserModel(UserCreationForm):
#     class Meta:
#         model=Account
#         fields=["first_name","last_name","email","username","password"]
