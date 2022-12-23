from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication
from rest_framework.decorators import permission_classes, authentication_classes
from .models import Post
from .serializers import PostSerializer

# Create your views here.


@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.BasicAuthentication])
class PostAPIView(APIView):
    def get(self, request):
        data = Post.objects.all()
        serializer = PostSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(
                instance=post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Post not found!!!"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response({"message": "Deleted"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Post not found!!!"}, status=status.HTTP_404_NOT_FOUND)
