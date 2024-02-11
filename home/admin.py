from django.contrib import admin
from home.models import Post, Member, Image, Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(Member) 
admin.site.register(Image)
admin.site.register(Comment)