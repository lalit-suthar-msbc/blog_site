from .models import Account
from django.forms import ModelForm
from django.contrib.auth import authenticate
from django.forms import forms
class UserModel(ModelForm):
    class Meta:
        model=Account
        fields=["first_name","last_name","email","username","password"]

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(email=username, password=password):
                raise forms.ValidationError("Invalid Login")