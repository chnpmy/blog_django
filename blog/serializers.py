from blog.models import Blog, Comment
from rest_framework import serializers


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("id", "title", "digest", "author", "ctime")


class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("id", "title", "article", "author", "ctime", "utime")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content", "ctime")
