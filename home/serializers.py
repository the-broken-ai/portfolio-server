from django.contrib.auth.models import Group, User
from rest_framework import serializers
from home.models import Post, Member, Image, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Member
        fields = ["user", "name", "username", "email", "github", "date_joined"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)
        member = Member.objects.create(user=user, **validated_data)
        return member

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")
        user = instance.user

        instance.name = validated_data.get("name", instance.name)
        instance.github = validated_data.get("github", instance.github)
        instance.save()

        user.username = user_data.get("username", user.username)
        user.email = user_data.get("email", user.email)
        user.save()

        return instance


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", queryset=Member.objects.all()
    )

    class Meta:
        model = Post
        fields = ["id", "title", "content", "cover_image", "author"]


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ["url", "title", "image", "date_posted", "author"]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ["url", "content", "date_posted", "author", "post"]


class ImagePostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ["url", "title", "image", "date_posted", "author"]
