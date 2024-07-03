from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from moviesapi.views import MovieViewSet, ActorViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'review', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies_api/', include(router.urls)),
]
