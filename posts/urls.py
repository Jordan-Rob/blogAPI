from django.urls import path

from .views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    path('posts/<int:pk>/', PostListAPIView.as_view(), name='posts'),
    path('posts/', PostDetailAPIView.as_view(), name='post')

]
