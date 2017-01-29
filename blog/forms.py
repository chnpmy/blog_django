# coding=utf-8
from django import forms
from blog.models import Blog


class BlogEditForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['id', 'title', 'digest', 'article']
