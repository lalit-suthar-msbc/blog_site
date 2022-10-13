from django.contrib import admin
from .models import Account
from .models import Blog
from .models import Category
admin.site.register(Account)
admin.site.register(Blog)
admin.site.register(Category)
# Register your models here.
