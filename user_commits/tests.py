from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class TestCommits(TestCase):

    def setUp(self):
        self.client = Client()

    """def test_user_commits(self):
        url = reverse('commits')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_commits.html')
        #self.assertContains(response, 'user_commits.html')"""
