#!/usr/bin/env python
# coding=utf-8
from django.db import models

# Create your models here.

USER_GROUP_CHOICE = (
    (0, "普通用户"),
    (1, "超级用户")
)


class UserModel(models.Model):
    user_name = models.CharField("用户名称", db_index=True, max_length=100, unique=True)
    user_password_md5 = models.CharField("用户密码", max_length=100)
    user_group = models.IntegerField("用户组别", choices=USER_GROUP_CHOICE, default=0)
    ctime = models.DateTimeField("创建时间", auto_now_add=True, db_index=True)
    utime = models.DateTimeField("更新时间", auto_now=True, db_index=True)

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = "用户"


class BlogModel(models.Model):
    title = models.CharField("博客标题", db_index=True, max_length=100)
    article = models.TextField("博客正文")
    author = models.CharField("作者", db_index=True, max_length=100)
    ctime = models.DateTimeField("创建时间", auto_now_add=True, db_index=True)
    utime = models.DateTimeField("更新时间", auto_now=True, db_index=True)

    class Meta:
        db_table = "blog"
        verbose_name = "博客"
        verbose_name_plural = "博客"


class CommentModel(models.Model):
    blog = models.ForeignKey(BlogModel)
    user = models.ForeignKey(UserModel)
    father = models.IntegerField("父评论", blank=True, default=-1, db_index=True)
    content = models.TextField("评论内容")
    ctime = models.DateTimeField("创建时间", auto_now_add=True, db_index=True)
    utime = models.DateTimeField("更新时间", auto_now=True, db_index=True)

    class Meta:
        db_table = "comment"
        verbose_name = "评论"
        verbose_name_plural = "评论"
