
from django.urls import path, include
from rest_framework import routers
from userauth import views as auth

router = routers.DefaultRouter()
router.register(r'users', auth.UserViewSet)
router.register(r'groups', auth.GroupViewSet)


urlpatterns = [
    path('router/', include(router.urls)),

    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include('djoser.urls.authtoken')),

    path('api-auth/', include('rest_framework.urls')),

]

# link.../token/login           POST Authorization and getting token
# link.../users/                POST Registration