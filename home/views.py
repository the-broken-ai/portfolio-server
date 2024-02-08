from django.shortcuts import render
from django.http import HttpResponse
from home import models

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the home index.")

def my_model_view(request):
    return 