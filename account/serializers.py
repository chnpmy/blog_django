from account.models import UserModel, BlogModel, CommentModel
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ("id", "user_name", "user_group")


class BlogListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogModel
        fields = ("id", "title", "digest", "author", "ctime")


class BlogDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogModel
        fields = ("id", "title", "article", "author", "ctime", "utime")


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommentModel
        fields = ("content", "ctime")
