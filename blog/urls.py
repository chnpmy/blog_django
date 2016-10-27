from django.conf.urls import url
from blog.views import BlogListView,\
    BlogDetailView, CommentListView

urlpatterns = [
    url(r'^$', BlogListView.as_view()),
    url(r'^blog/$', BlogListView.as_view()),
    url(r'^blog/(?P<blog_id>[0-9]+)/$', BlogDetailView.as_view()),
    url(r'^comment/(?P<blog_id>[0-9]+)/$', CommentListView.as_view()),
]