from django.shortcuts import render
from blog.models import BlogModel, CommentModel
from blog.serializers import BlogListSerializer, BlogDetailSerializer,\
    CommentSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.views.generic import ListView, DetailView

# Create your views here.


class BlogListAPIView(ListAPIView):
    queryset = BlogModel.objects.all().order_by("-ctime")
    serializer_class = BlogListSerializer


class BlogDetailAPIView(RetrieveAPIView):
    serializer_class = BlogDetailSerializer

    def get_queryset(self):
        blog_id = self.request.query_params.get("blog_id")
        return BlogModel.objects.get(id=blog_id)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = None

    def get_queryset(self):
        blog_id = self.request.query_params.get("blog_id")
        return CommentModel.objects.filter(commentmodel__blog_id=blog_id)


class BlogListView(ListView):
    model = BlogModel
    template_name = 'blog_list.html'


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'blog_detail.html'

    def get_object(self, queryset=None):
        return BlogModel.objects.get(id=self.kwargs["blog_id"])


class CommentListView(ListView):
    model = CommentModel
