from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getpersoninfo/", views.json_personInfo, name="return_json"),
    path("getpostinfo/", views.json_PostInfo, name="return_json"),
    path("post/",views.submit, name="submit"),
    path("person/", views.PersonList.as_view(), name="person_list"),
]