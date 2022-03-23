from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from base64 import b64encode as enc64
from base64 import b64decode as dec64

from .image_processing import Image as Img
from del_photos.settings import MEDIA_ROOT
from app.models import Post, Image, Reaction, Size, Comment
from app.serializers import (
    PostSerializer, CommentSerializer, ReactionSerializer,
    SizeSerializer, ImageSerializer
)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReactionViewSet(ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer

    def get(self, request, pk, *args, **kwargs):
        reaction = Reaction.objects.get(id=pk)
        # if reaction.user == 
        return super().get(self, request, *args, **kwargs)

    def destroy(self, *args, **kwargs):
        return super().destroy(self, *args, **kwargs)


class SizeViewSet(ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        print(dir(request))
        print(request.POST)
        if 'effect' in request.POST.keys():
            effect = request.POST['effect']
            img = Image.objects.create(
                image = request.FILES['image'],
                post=Post.objects.get(id=request.POST['post'])
            )
            print(dir(img))
            print(img.image)

            if effect == 'blur':

                path = ''.join([MEDIA_ROOT, str(img.image)])
                print(path)
                after_effect = Img(path)
                after_effect.Blur()
                after_effect.image.save(path)

            arg = {
                'id': img.pk,
                'image': path,
                'status': 2022
            }

            return Response(arg, status=201)

        return super().create(request, *args, **kwargs)




