from django.contrib import admin
from account.models import UserModel, BlogModel, CommentModel


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    exclude = ["article"]

admin.site.register(UserModel)
admin.site.register(BlogModel)
admin.site.register(CommentModel)
