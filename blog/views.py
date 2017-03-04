from blog.forms import BlogEditForm, PictureUploadForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from blog.models import Blog, Comment
from blog.serializers import BlogListSerializer, BlogDetailSerializer,\
    CommentSerializer
from django.views.generic import FormView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.views.generic import ListView, DetailView, CreateView
import markdown2
from blog.models import Picture

# Create your views here.


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all().order_by("-ctime")
    serializer_class = BlogListSerializer


class BlogDetailAPIView(RetrieveAPIView):
    serializer_class = BlogDetailSerializer

    def get_queryset(self):
        blog_id = self.request.query_params.get("blog_id")
        return Blog.objects.get(id=blog_id)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = None

    def get_queryset(self):
        blog_id = self.request.query_params.get("blog_id")
        return Comment.objects.filter(comment__blog_id=blog_id)


class BlogListView(ListView):
    paginate_by = 5
    model = Blog
    template_name = 'blog_list.html'

    def get_queryset(self):
        query_set = super(BlogListView, self).get_queryset().order_by("-ctime")
        if self.request.GET.get("search"):
            query_set = query_set.filter(title__contains=self.request.GET.get("search"))
        for each in query_set:
            each.digest = markdown2.markdown(each.digest)
        return query_set


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Blog, id=self.kwargs.get("blog_id"))
        # obj.article = markdown2.markdown(obj.article)
        return obj


class BlogEditView(LoginRequiredMixin, FormView):
    template_name = 'blog_edit.html'
    form_class = BlogEditForm

    def get_initial(self):
        initial = super(BlogEditView, self).get_initial()
        if self.kwargs.get("blog_id"):
            obj = get_object_or_404(Blog, id=self.kwargs.get("blog_id"))
            initial["id"] = obj.id
            initial["title"] = obj.title
            initial["digest"] = obj.digest
            initial["article"] = obj.article
        return initial

    def form_valid(self, form):
        blog_id = self.update_blog(form)
        return HttpResponseRedirect(reverse("blog_detail", kwargs={"blog_id": blog_id}))

    def update_blog(self, form):
        fields = form.cleaned_data
        if self.kwargs.get("blog_id"):
            obj = get_object_or_404(Blog, id=self.kwargs["blog_id"])
        else:
            obj = Blog()
            obj.author = self.request.user
        for k, v in fields.items():
            setattr(obj, k, v)
        obj.save()
        return obj.id

    def get(self, request, *args, **kwargs):
        if self.kwargs.get("blog_id"):
            obj = get_object_or_404(Blog, id=self.kwargs.get("blog_id"))
            if obj.author != request.user:
                raise PermissionError
        return super(BlogEditView, self).get(request, *args, **kwargs)


class CommentListView(ListView):
    model = Comment


class PictureListView(ListView, LoginRequiredMixin):
    model = Picture
    paginate_by = 100
    template_name = "blog_picture_list.html"

    def get_queryset(self):
        query_set = super(PictureListView, self).get_queryset().order_by("-ctime")
        query_set = query_set.filter(user=self.request.user)
        return query_set


class PictureUploadView(FormView, LoginRequiredMixin):
    template_name = "blog_picture_upload.html"
    form_class = PictureUploadForm

    def form_valid(self, form):
        fields = form.cleaned_data
        picture = Picture()
        picture.user = self.request.user
        picture.url = fields["picture"]
        picture.save()
        return HttpResponseRedirect(reverse("blog_picture_list"))

    def get(self, request, *args, **kwargs):
        return super(PictureUploadView, self).get(request, *args, **kwargs)


