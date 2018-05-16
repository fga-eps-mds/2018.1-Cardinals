from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class RepoInfoTests(TestCase):

    def test_get_repo_name(self):

        organization = 'fga-gpp-mds'
        repo_name = '2018.1-Cardinals'
        repo_path = organization + '/' + repo_name

        url = reverse('getRepoInfo')

        response =  self.client.post(url, {'repository': repo_path})

        response_repo_name = response.context['repo'].name

        self.assertEquals(repo_name, response_repo_name)