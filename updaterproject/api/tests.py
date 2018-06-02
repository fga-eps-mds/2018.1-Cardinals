from django.test import TestCase, Client
from api.views import API

class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_repository_endpoint_200(self):
        pass

    def tearDown(self):
        pass