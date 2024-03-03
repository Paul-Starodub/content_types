from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from tracking.models import Post
from tracking.serializers import PostSerializer


# class PostListView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#
#         # Create a serializer instance for the list of posts with specific fields
#         serializer = PostSerializer(
#             instance=posts, many=True, fields=["title"]
#         )
#
#         serialized_data = serializer.data
#
#         return Response(serialized_data)


# With this setup, you can make requests to /api/posts/ and include the fields parameter in the query string to dynamically choose the fields you want to include in the response. For example, /api/posts/?fields=title,content.


class DynamicFieldsModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer(self, *args: tuple, **kwargs: dict) -> PostSerializer:
        fields = self.request.query_params.get("fields", None)
        kwargs["context"] = self.get_serializer_context()
        return self.serializer_class(fields=fields, *args, **kwargs)
