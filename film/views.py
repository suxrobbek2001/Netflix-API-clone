from django.contrib.postgres.search import TrigramSimilarity
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Actor, Movie, Comment
from django.http import JsonResponse
from rest_framework.views import APIView

from .serializers import ActorSerializer, MovieSerializer, CommentSerializer


class Home(APIView):
    def get(selfself, request):
        xabar = {"massage": "Hello World"}
        return JsonResponse(xabar)

    def post(self, request):
        xabar = {"message": "Jo'natgan xabarangiz qabul qilindi"}
        return JsonResponse(xabar)

# class ActorAPIView(APIView):
#     def get(self, request):
#         actors = Actor.objects.all()
#         ser = ActorSerializer(actors, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         actor = request.data
#         ser = ActorSerializer(data=actor)
#         if ser.is_valid():
#             ser.save()
#         return Response(ser.data)
#
#     def delete(self, request, son):
#         actor = Actor.objects.get(id=son)
#         actor.delete()
#         return JsonResponse({"xabar": "Berilgan habarda actor o'chirildi"})
#
#     def put(self, request, son):
#         actor = Actor.objects.get(id=son)
#         ser = ActorSerializer(actor, data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return JsonResponse({"xabar": "O'zgarishi amaga oshmadi"})



# class MovieAPIView(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         ser = MovieSerializer(movies, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         movie = request.data
#         ser = MovieSerializer(data=movie)
#         if ser.is_valid():
#             ser.save()
#         return Response(ser.data)
#
#     def delete(self, request, son):
#         movie = Movie.objects.get(id=son)
#         movie.delete()
#         return JsonResponse({"xabar": "Berilgan habarda movie o'chirildi"})
#
#     def put(self, request, son):
#         movie = Movie.objects.get(id=son)
#         ser = MovieSerializer(movie, data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return JsonResponse({"xabar": "O'zgarishi amaga oshmadi"})
#
#     def patch(self, request, son):
#         movie = Movie.objects.get(id=son)
#         ser = MovieSerializer(movie, data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return JsonResponse({"xabar": "O'zgarishi amaga oshmadi"})

class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get_queryset(self):
        actors = Actor.objects.all()
        soz = self.request.query_params.get("search")
        if soz is not None:
            actors = Actor.objects.annotate(
                similarity=TrigramSimilarity("name", soz)
            ).filter(similarity__gte=0.4).order_by("-similarity")
        return actors

    @action(detail=True, methods=['GET'])
    def actors(self, request, *args, **kwargs):
        actor = self.get_object()
        ac = Movie.objects.filter(actor=actor)
        ser = MovieSerializer(ac, many=True)
        return Response(ser.data)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter, OrderingFilter, ]
    ordering_fields = ["data", "title", ]
    search_fields = ["title", ]

    @action(detail=True, methods=['GET'])
    def movies(self, request, *args, **kwargs):
        movie = self.get_object()
        ac = Actor.objects.filter(id=movie.actor.id)
        ser = ActorSerializer(ac, many=True)
        return Response(ser.data)

    @action(detail=True, methods=['GET'])
    def comments(self, request, *args, **kwargs):
        movie = self.get_object()
        com = Comment.objects.filter(movie=movie)
        ser = CommentSerializer(com, many=True)
        return Response(ser.data)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



