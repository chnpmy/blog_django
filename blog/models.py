from django.db import models
from django.conf import settings

# Create your models here.


class Blog(models.Model):
    title = models.CharField("博客标题", db_index=True, max_length=100)
    digest = models.TextField("博客摘要")
    article = models.TextField("博客正文")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True, max_length=100)
    ctime = models.DateTimeField("创建时间", auto_now_add=True, db_index=True)
    utime = models.DateTimeField("更新时间", auto_now=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "blog"
        verbose_name = "博客"
        verbose_name_plural = "博客"


class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    father = models.ForeignKey("Comment", blank=True, db_index=True)
    content = models.TextField("评论内容")
    ctime = models.DateTimeField("创建时间", auto_now_add=True, db_index=True)
    utime = models.DateTimeField("更新时间", auto_now=True, db_index=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "comment"
        verbose_name = "评论"
        verbose_name_plural = "评论"


class Picture(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    url = models.FileField("图片地址", null=False, max_length=500, upload_to="pic/")
    ctime = models.DateTimeField("创建时间", auto_now_add=True, db_index=True)
    utime = models.DateTimeField("更新时间", auto_now=True, db_index=True)

    def __str__(self):
        return self.url

    class Meta:
        db_table = "picture"
        verbose_name = "图片"
        verbose_name_plural = "图片"
