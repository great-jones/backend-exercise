from django.contrib.auth.models import User
from django.db import models

# Create model here
from django.db.models import ForeignKey, deletion

"""
Comment Model
 foreign key to user 
 text 
"""

class Comment(models.Model):
    text = models.TextField()