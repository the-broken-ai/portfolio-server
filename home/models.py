from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(Member)
    
    def __str__(self):
        return self.title