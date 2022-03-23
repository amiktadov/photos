from django.utils import timezone
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from base64 import b64encode as enc64
from base64 import b64decode as dec64

from .image_processing import Image as Img
from del_photos.settings import MEDIA_ROOT, MEDIA_URL
from app.models import Post, Image, Reaction, Size, Comment
from app.serializers import (
    PostSerializer, CommentSerializer, ReactionSerializer,
    SizeSerializer, ImageSerializer
)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.filter(date_del__isnull=True)
    serializer_class = CommentSerializer

    def destroy(self, request, pk, *args, **kwargs):
        reaction = Comment.objects.get(id=pk)
        reaction.date_del = timezone.now()
        reaction.save()
        return Response(status=202)


class ReactionViewSet(ModelViewSet):
    queryset = Reaction.objects.filter(date_del__isnull=True)
    serializer_class = ReactionSerializer

    def destroy(self, request, pk, *args, **kwargs):
        reaction = Reaction.objects.get(id=pk)
        reaction.date_del = timezone.now()
        reaction.save()
        return Response(status=202)


class SizeViewSet(ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def retrieve(self, request, pk, *args, **kwargs):
        image = self.queryset.get(id=pk)
        path = ''.join([MEDIA_ROOT, str(image.image)])
        with open(path , 'rb') as i:
            base = enc64(i.read())
        arg = {
            "id": pk,
            "path": MEDIA_URL+str(image.image),
            "base64": base,
            "coords": image.coords,
            "post": image.post.pk
        }
        return Response(arg, status=201)

    def create(self, request, *args, **kwargs):
        if 'effect' in request.POST.keys():
            
            if request.FILES['image']:
                image = request.FILES['image']
            else:
                image = request.POST['image']
                image = dec64(image)

            img = Image.objects.create(
                image=image,
                post=Post.objects.get(id=request.POST['post'])
            )

            effect = request.POST['effect']
            path = ''.join([MEDIA_ROOT, str(img.image)])
            after_effect = Img(path)

            if effect == 'blur':
                after_effect.Blur()

            after_effect.image.save(path)

            arg = {
                'id': img.pk,
                'image': path,
                'status': 2022
            }

            return Response(arg, status=201)

        return super().create(request, *args, **kwargs)




