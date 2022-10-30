from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(User):
    pass
class Comment(models.Model):
    comment = models.IntegerField(default=0)
