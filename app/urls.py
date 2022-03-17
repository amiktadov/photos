from django.urls import path, include

from app import views as app


urlpatterns = [
    path('get-posts/', app.PostViewSet.as_view()),
    path('get-posts/<int:post_pk>/', app.GetPostAPI.as_view()),
]