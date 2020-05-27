from django.urls import path

from .views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post')

]
