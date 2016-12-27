from django.conf.urls import url, include
import django.contrib.auth.views as views
from account.views import logout

urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/', views.login, name='login'),
]
