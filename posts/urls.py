from django.urls import path

from .views import PostListAPIView, PostDetailAPIView, UserListView, UserDetailView

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post'),
    path('users/', UserListView.as_view(), name='users'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user')

]
