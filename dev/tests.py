from django.test import TestCase


class TestViews(TestCase):

    def test_template_develops(self):
        self.assertTemplateUsed('templates/develops.html')
