from django.contrib import admin
from .models import Post, Comment, Profile

admin.site.register(Post)
admin.site.register(Comment)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'info', 'avatar', 'gender']

admin.site.register(Profile, UserProfileAdmin)