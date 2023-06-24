from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Testing and debugging Models

class Item(models.Model):
    name = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)
    
class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)

# Models to store Templates

class WorkoutTemplate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workoutTitle = models.CharField(max_length=100)
    
    def __str__(self):
        return self.workoutTitle
    
class ExerciseTemplate(models.Model):
    workoutTemplate = models.ForeignKey(WorkoutTemplate, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.CharField(max_length=100)
    
    def __str__(self):
        return self.exercise