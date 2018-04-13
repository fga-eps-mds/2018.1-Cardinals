from django.test import TestCase

# Create your tests here.
class TestCommits(TestCase):

    def setUp(self):
        self.client = Client()

    def test_user_commits(self):
        url = reverse('user_commits')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'allCommits')
