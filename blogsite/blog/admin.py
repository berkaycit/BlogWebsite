from django.contrib import admin
from .models import Post, Comment, Profile, Like

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'info', 'avatar', 'gender']

admin.site.register(Profile, UserProfileAdmin)