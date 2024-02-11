from django.db import models
from django.contrib.auth.models import Group, User
from django.utils import timezone

# Create your models here.


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    github = models.URLField(max_length=200, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='posts/', blank=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
    
