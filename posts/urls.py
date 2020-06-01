from django.urls import path

#from .views import PostListAPIView, PostDetailAPIView, UserListView, UserDetailView

from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

"""
urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post'),
    path('users/', UserListView.as_view(), name='users'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user')

]
"""

Router = SimpleRouter()

Router.register('users', UserViewSet, )
Router.register('', PostViewSet, )

urlpatterns = Router.urls
