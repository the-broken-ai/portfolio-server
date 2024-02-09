from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from home.models import Person, Post

from rest_framework.generics import ListAPIView
from home.models import Person, Post
from home.serializers import PersonSerializer, PostSerializer


# Create your views here.
class PersonList(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def index(request):
    return render(request, "index.html")

def json_personInfo(request):
    persons = Person.objects.all()
    persons_list = []
    for person in persons:
        firstName = person.first_name
        lastName = person.last_name
        username = person.username
        email = person.email
        phone = person.phone
        address = person.address
        github = person.github
        persons_list.append({
            "firstName": firstName,
            "lastName": lastName,
            "username": username,
            "email": email,
            "phone": phone,
            "address": address,
            "github": github,
        })
    return JsonResponse(persons_list, safe=False)

def json_PostInfo(request):
    posts = Post.objects.all()
    posts_list = []
    for post in posts:
        title = post.title
        content = post.content
        contributor = post.contributor
        date_uploaded = post.date_uploaded
        url = post.url
        posts_list.append({
            "title": title,
            "content": content,
            "contributor": contributor,
            "date_uploaded": date_uploaded,
            "url": url,
        })
    return JsonResponse(posts_list, safe=False)

def submit(request):

    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        github = request.POST.get("github")

        person = models.Person(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            address=address,
            github=github,
        )
        person.save()
    return render(request, "/")