from rest_framework.response import Response
from rest_framework.views import APIView

from tracking.models import Post
from tracking.serializers import PostSerializer


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()

        # Create a serializer instance for the list of posts with specific fields
        serializer = PostSerializer(
            instance=posts, many=True, fields=["title"]
        )

        serialized_data = serializer.data

        return Response(serialized_data)
