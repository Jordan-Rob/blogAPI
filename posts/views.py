from rest_framework import generics

from .models import Post

# Create your views here.


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
