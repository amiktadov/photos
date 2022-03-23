from django.urls import path, include
from rest_framework import routers

from app import views as app


router = routers.SimpleRouter()
router.register('posts', app.PostViewSet)
router.register('comments', app.CommentViewSet)
router.register('reactions', app.ReactionViewSet)
router.register('sizes', app.SizeViewSet)
router.register('images', app.ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]