from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from .permissions import IsAuthorOrReadOnly

from .models import Post
from .serializers import PostSerializer, UserSerializer

# Create your views here.


class PostListAPIView(generics.ListCreateAPIView):

    # view-level permissions
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    # view-level permissions
    # permission_classes = (permissions.IsAuthenticated,)

    # custom permissions
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
