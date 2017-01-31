# coding=utf-8
from django import forms
from blog.models import Blog, Picture


class BlogEditForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['id', 'title', 'digest', 'article']


class PictureUploadForm(forms.ModelForm):
    picture = forms.FileField()

    class Meta:
        model = Picture
        fields = []
