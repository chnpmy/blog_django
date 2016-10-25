from django.contrib import admin
from account.models import UserModel, BlogModel, CommentModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(BlogModel)
admin.site.register(CommentModel)
