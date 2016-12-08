from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from account.views import logout

urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^', include('django.contrib.auth.urls')),
]
