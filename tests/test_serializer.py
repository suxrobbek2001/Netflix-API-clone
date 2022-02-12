from unittest import TestCase

from film.models import Actor, Movie
from film.serializers import ActorSerializer, MovieSerializer

# class TestArtistSerializer(TestCase):
#     def setUp(self) -> None:
#         Artist.objects.create(
#             name="li",
#             yonalish="Rep",
#             description="afafwefssdggsgsf"
#         )
#
#     def test_artist(self):
#         a = Artist.objects.all()
#         malumot = ArtistSerializer(a, many=True)
#         self.assertTrue(malumot.data[0]["id"] == 1)
#         self.assertEqual(malumot.data[0]["id"], 1)




# class TestActorModels(TestCase):
#         def setUp(self) -> None:
#             pass
#             # Actor.objects.create(
#             #     name="Suxrobbek",
#             #     birth_data="2001-08-13",
#             #     gender="erkak"
#             # )
#
#         def test_act(self):
#             a = Actor.objects.all()
#             assert a[4].name == "Suxrobbek"
#             assert a[4].gender == "erkak"
#
#
#
#
# class TestActortSerializer(TestCase):
#     def setUp(self) -> None:
#         pass
#     def test_actor(self):
#         a = Actor.objects.all()
#         malumot = ActorSerializer(a, many=True)
#         assert malumot.data[0]["id"] == 1
#         assert malumot.data[0]["name"] == "ROBERT DOWNEY, JR."
#         assert malumot.data[0]["birth_data"] == "1965-04-04"
#         assert malumot.data[0]["gender"] == "erkak"
#
#
#     def test_movie(self):
#         a = Movie.objects.all()
#         malumot = MovieSerializer(a, many=True)
#         assert malumot.data[0]["id"] == 1
#         assert malumot.data[0]["title"] == "AVENGERS: INFINITY WAR (2018)"
#         assert malumot.data[0]["janr"] == "action"
#         assert malumot.data[0]["data"] == "2018-06-25"
#
#
#         assert malumot.data[1]["id"] == 2
#         assert malumot.data[1]["title"] == "AVENGERS: INFINITY WAR (2018)"
#         assert malumot.data[1]["janr"] == "action"
#         assert malumot.data[1]["data"] == "2018-06-25"
#
