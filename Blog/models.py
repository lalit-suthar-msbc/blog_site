from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.models import AbstractUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have email")
        if not username:
            raise ValueError("Users must have username")
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    id=models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, verbose_name='email', unique=True)
    username = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(verbose_name='Date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # profile_image = models.ImageField(max_length=300, upload_to='images/profiles', null=True, blank=True,
    #                                   default='images/default_user_image.png')
    hide_email = models.BooleanField(default=True)
    groups = models.ManyToManyField(blank=True,
                                    help_text='The groups this user belongs to. A user will get all permissions '
                                              'granted to each of their groups.',
                                    related_name='user_set_custom', related_query_name='user', to='auth.Group',
                                    verbose_name='groups')
    user_permissions = models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                              related_name='user_set_custom', related_query_name='user',
                                              to='auth.Permission',
                                              verbose_name='user permissions')
    dob = models.DateField(null=True)
    city = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    phone = models.CharField(default='+91', max_length=15)
    address = models.CharField(max_length=500)
    gender = models.CharField(max_length=10)
    termsAgreed = models.CharField(max_length=5)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name}"


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=500)
    slug = models.CharField(unique=True, max_length=500)
    author = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    # img_file = models.ImageField(upload_to='images/blog')
    posted_on = models.DateField(auto_now_add=True)
    last_edit = models.DateField(auto_now_add=True, null=True)
    content = models.CharField(max_length=10000)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    hidden = models.BooleanField(default=False)
    viewers = models.ManyToManyField(to=Account, related_name='post_viewers')

    def __str__(self):
        return f"{self.title[:50]} by {self.author}"
