from blog.models import BlogModel, CommentModel
from rest_framework import serializers


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ("id", "title", "digest", "author", "ctime")


class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ("id", "title", "article", "author", "ctime", "utime")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ("content", "ctime")
