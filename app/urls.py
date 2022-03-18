from django.urls import path, include
from rest_framework import routers

from app import views as app


router = routers.SimpleRouter()
router.register('posts', app.PostViewSet)
router.register('comments', app.CommentViewSet)
router.register('reactions', app.ReactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]