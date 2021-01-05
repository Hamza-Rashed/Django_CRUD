
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default=' ') 
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
