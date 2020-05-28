from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer

# Create your views here.


class PostListAPIView(generics.ListCreateAPIView):

    # view-level permissions
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    # view-level permissions
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer
