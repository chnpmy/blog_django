from django.shortcuts import render
from account.models import BlogModel, CommentModel
from account.serializers import BlogListSerializer,\
    BlogDetailSerializer, CommentSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


# Create your views here.
class BlogListView(ListAPIView):
    queryset = BlogModel.objects.all().order_by("-ctime")
    serializer_class = BlogListSerializer


class BlogDetailView(RetrieveAPIView):
    serializer_class = BlogDetailSerializer

    def get_queryset(self):
        blog_id = self.request.query_params.get("blog_id")
        return BlogModel.objects.get(id=blog_id)


class CommentListView(ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = None

    def get_queryset(self):
        blog_id = self.request.query_params.get("blog_id")
        return CommentModel.objects.filter(commentmodel__blog_id=blog_id)
