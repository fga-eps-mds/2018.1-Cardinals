from django.test import TestCase


class TestTemplates(TestCase):
    def test_template_contributors(self):
            self.assertTemplateUsed('templates/contributors.html')
