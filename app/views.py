from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from app.models import Post, Image, Reaction, Size, Comment
from app.serializers import PostsSerializer, PostSerializer


class PostViewSet(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]


class PostsAPI(APIView):
    """ Получение всех постов и создание постов """

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        post = PostSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response(status=201)
        else:
            return Response(status=401)

    
class GetPostAPI(APIView):
    """" Получение конкретного поста, его изменение и удаление """

    def get(self, request, post_pk):
        post = Post.objects.get(id=post_pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

