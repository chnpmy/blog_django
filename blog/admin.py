from django.contrib import admin
from blog.models import Blog, Comment


# Register your models here.
#class BlogAdmin(admin.ModelAdmin):
#    exclude = ["article"]

admin.site.register(Blog)
admin.site.register(Comment)
