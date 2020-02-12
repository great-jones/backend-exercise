from django.apps import AppConfig
from django.contrib.auth.models import User


class CommentsConfig(AppConfig):
    name = 'comments'
    User.objects.create_user()
