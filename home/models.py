from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    github = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True)
    repository = models.URLField(max_length=100, blank=True, null=True)
    contributors = models.ManyToManyField(User, related_name='contributors', blank=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
    
