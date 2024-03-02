from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    GenericRelation,
)
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=266)
    content = models.TextField()
    likes = GenericRelation("Like", related_query_name="post")

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField()
    likes = GenericRelation("Like")

    def __str__(self) -> str:
        return self.content[:24]


class Like(models.Model):
    is_liked = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self) -> str:
        return str(self.is_liked)
