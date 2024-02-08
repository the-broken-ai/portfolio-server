from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    github = models.URLField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    contributor = models.ForeignKey(Person, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    url = models.URLField()

    def __str__(self):
        return self.title
