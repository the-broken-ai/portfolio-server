from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.contrib.auth.models import Group, User

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from home.models import Post, Member, Image, Comment

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions, viewsets

from home.serializers import GroupSerializer, UserSerializer, PostSerializer, MemberSerializer, SubmitSerializer, ImageSerializer, CommentSerializer, ImagePostSerializer


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows images to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ImagePostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows imageposts to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImagePostSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class SubmitViewSet(APIView):
    """
    API endpoint that allows members to be submitted.
    """
    def post(self, request, format=None):
        serializer = SubmitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
@require_http_methods(["POST"])
def submit(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        github = request.POST.get("github")
        
        member = Member(name=name, email=email, password=password, github=github)
        member.save()
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "failed"})
    

def index(request):
    return redirect("http://192.168.2.21:3000")




class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id})