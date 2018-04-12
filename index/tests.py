from django.test import TestCase, Client


class TestViews(TestCase):

    def setUp(self):
        self.c = Client()

    def test_template_index(self):
        self.assertTemplateUsed('templates/index.html')

    def test_searchRepository(self):
        data = {
            'repository': 'fga-gpp-mds/2018.1-Cardinals',
        }
        response = self.c.post('/pyGithub/getContributors/', data)
        self.assertEquals(200, response.status_code)
