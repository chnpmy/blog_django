from django.conf.urls import url
from blog.views import BlogListView,\
    BlogDetailView, CommentListView, BlogEditView

urlpatterns = [
    url(r'^$', BlogListView.as_view()),
    url(r'^blog/$', BlogListView.as_view()),
    url(r'^blog/(?P<blog_id>[0-9]+)/$', BlogDetailView.as_view(), name="blog_detail"),
    url(r'blog/add/$', BlogEditView.as_view(), name="blog_add"),
    url(r'blog/(?P<blog_id>[0-9]+)/edit/$', BlogEditView.as_view(), name="blog_edit"),
    url(r'^comment/(?P<blog_id>[0-9]+)/$', CommentListView.as_view()),
]