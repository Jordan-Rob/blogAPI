from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    model = Post
    fields = ('author', 'title', 'body', 'created_at')
