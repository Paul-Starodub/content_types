from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from tracking.models import Post, Comment, Like


class LikeInline(GenericTabularInline):
    model = Like
    max_num = 3


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content")
    inlines = [LikeInline]


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "content")
    inlines = [LikeInline]


class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "is_liked",
        "content_type",
        "object_id",
        "content_object",
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
