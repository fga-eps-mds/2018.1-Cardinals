from django.test import TestCase


# Create your tests here.
class TestViews(TestCase):

    def test_template_develops(self):
        self.assertTemplateUsed('templates/develops.html')
        