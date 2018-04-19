from django.test import TestCase, Client


class TestViews(TestCase):

    def setUp(self):
        self.c = Client()

    def test_template_index(self):
        self.assertTemplateUsed('templates/index.html')
