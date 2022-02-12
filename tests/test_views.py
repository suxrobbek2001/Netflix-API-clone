from django.test import Client
from unittest import TestCase


class TestActorViews(TestCase):
    def setUp(self) -> None:
        self.cl = Client()

    def test_get_actor(self):
        natija = self.cl.get("/actor/1/")
        assert natija.status_code == 200
        m = natija.data
        print(m)
        self.assertTrue(len(m) !=0)
        self.assertEqual(m["name"], "ROBERT DOWNEY, JR.")
        self.assertEqual(m['birth_data'], '1965-04-04')
        self.assertEqual(m['gender'], 'erkak')


