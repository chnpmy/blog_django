from blog.forms import BlogEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from blog.models import BlogModel, CommentModel
from blog.serializers import BlogListSerializer, BlogDetailSerializer,\
    CommentSerializer
from django.views.generic import FormView
from django.views.generic import View
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
        obj = get_object_or_404(BlogModel, id=self.kwargs.get("blog_id"))
        obj.article = markdown2.markdown(obj.article)
        return obj


class BlogEditView(LoginRequiredMixin, FormView):
    template_name = 'blog_edit.html'
    form_class = BlogEditForm

    def get_initial(self):
        initial = super(BlogEditView, self).get_initial()
        if self.kwargs.get("blog_id"):
            obj = get_object_or_404(BlogModel, id=self.kwargs.get("blog_id"))
            initial["id"] = obj.id
            initial["title"] = obj.title
            initial["digest"] = obj.digest
            initial["article"] = obj.article
        return initial

    def form_valid(self, form):
        self.update_blog(form)
        return HttpResponseRedirect(reverse("blog_detail", kwargs={"blog_id": self.kwargs.get("blog_id")}))

    def update_blog(self, form):
        fields = form.cleaned_data
        obj = get_object_or_404(BlogModel, id=self.kwargs["blog_id"])
        for k, v in fields.items():
            setattr(obj, k, v)
        obj.save()


class CommentListView(ListView):
    model = CommentModel
