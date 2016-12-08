from django.shortcuts import render
import django.contrib.auth.views as views


# Create your views here.
def logout(request):
    return views.logout(request, next_page="/")
