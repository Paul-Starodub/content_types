from django.urls import path

from tracking.views import PostListView


urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
]

app_name = "tracking"
