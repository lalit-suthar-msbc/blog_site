from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = "this file runs successfully"

    def add_arguments(self, parser):
        # parser.add_argument('username', action="store_true", help='it shows username')
        # parser.add_argument('show_user', action='store_true', help='it shows username')
        parser.add_argument('-a', "--name", type=str, help='username')
        parser.add_argument('-b', "--user", type=str, help='username')
        parser.add_argument('-c', "--username", type=str, help='username')

    def handle(self, *args, **kwargs):

        name = kwargs['name']
        user = kwargs['user']
        username = kwargs['username']

        if user:
            User_ = get_user_model()
            User = User_.objects.all()
            print(User)
        if username:
            User_ = get_user_model()
            User_ = User_.objects.get(username=name)
            User_.delete()
            print("user deleted successfully")
