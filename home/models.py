from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30, default="John")
    last_name = models.CharField(max_length=30, default="Doe")
    username = models.CharField(max_length=30, default="sujannibba")
    email = models.EmailField(default="sujan@nibba.com")
    phone = models.CharField(max_length=15, default="1234567890")
    address = models.CharField(max_length=100, default="1234 Main St")
    github = models.URLField(default="github.com/sujan-nibba")

    def __str__(self):
        return self.first_name + " " + self.last_name

class Post(models.Model):
    title = models.CharField(max_length=100, default="Title")
    content = models.TextField(default="Content")
    contributor = models.ForeignKey(Person, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    url = models.URLField(default="https://www.google.com")

    def __str__(self):
        return self.title
