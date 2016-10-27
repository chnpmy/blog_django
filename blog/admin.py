from django.contrib import admin
from blog.models import BlogModel, CommentModel


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    exclude = ["article"]

admin.site.register(BlogModel, BlogAdmin)
admin.site.register(CommentModel)