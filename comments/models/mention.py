from django.contrib.auth.models import User
from django.db import models

from comments.models import Comment


class Mention(models.Model):
    user = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING)
    comment = models.ForeignKey(Comment, on_delete=models.deletion.DO_NOTHING)
