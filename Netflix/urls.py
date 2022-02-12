from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from film.views import Home, ActorViewSet, MovieViewSet, CommentViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Netflix clone API",
      default_version='v1',
      description="Netflixni clone versiyasi",
      contact=openapi.Contact("Sukhrobbek Mukhammadjonov <surobbekmuxammadjonov2gmail.com>, <+998993930242>"),
   ),
   public=True,
)

router = DefaultRouter()
router.register("movie", MovieViewSet)
router.register("actor", ActorViewSet)
router.register("comment", CommentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home.as_view()),
    # path('actor/', ActorAPIView.as_view()),
    # path('actor/<int:son>/', ActorAPIView.as_view()),
    # path('movie/', MovieAPIView.as_view()),
    # path('movie/<int:son>/', MovieAPIView.as_view()),
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui("swagger", cache_timeout=0), name="swagger-doc"),
    path('doc/', schema_view.with_ui("redoc", cache_timeout=0), name="redoc-doc"),

]

