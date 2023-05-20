from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)
    
class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)