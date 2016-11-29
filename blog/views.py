from django.shortcuts import render
from blog.models import BlogModel, CommentModel
from blog.serializers import BlogListSerializer, BlogDetailSerializer,\
    CommentSerializer
from django.views.generic import FormView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.views.generic import ListView, DetailView
import markdown2

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

    def get_queryset(self):
        query_set = super(BlogListView, self).get_queryset()
        for each in query_set:
            each.digest = markdown2.markdown(each.digest)
        return query_set


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'blog_detail.html'

    def get_object(self, queryset=None):
        obj = BlogModel.objects.get(id=self.kwargs["blog_id"])
        obj.article = markdown2.markdown(obj.article)
        return obj


class BlogEditView(FormView):
    template_name = "blog_edit.html"


class CommentListView(ListView):
    model = CommentModel
