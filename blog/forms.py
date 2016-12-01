# coding=utf-8
from django import forms
from blog.models import BlogModel


class BlogEditForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        fields = ['id', 'title', 'digest', 'article']
