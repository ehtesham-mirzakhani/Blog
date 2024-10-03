from django.contrib import admin

from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at','photo')
    list_editable = ('author',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'body', 'created_at')

# Register your models here.
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)