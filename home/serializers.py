from django.contrib.auth.models import Group, User
from rest_framework import serializers
from home.models import Post, Member, Image, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
        
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'title', 'content', 'date_posted', 'author', 'cover_image', 'repository', 'contributors']
        
class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['url', 'name', 'email', 'password', 'github', 'date_joined', 'username']
        
    
class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['url', 'title', 'image', 'date_posted', 'author']
        
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'content', 'date_posted', 'author', 'post']
        
class ImagePostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['url', 'title', 'image', 'date_posted', 'author']
        
        
class SubmitSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
    github = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Member.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.github = validated_data.get('github', instance.github)
        instance.save()
        return instance