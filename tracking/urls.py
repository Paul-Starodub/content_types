from django.urls import path, include
from rest_framework import routers

from tracking.views import DynamicFieldsModelViewSet

router = routers.DefaultRouter()
router.register("posts", DynamicFieldsModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "tracking"
