from django.test import TestCase
from django.urls import reverse
from oauth.credentials import get_credentials

from github import Github


class SetUp:
    organization = 'fgacardinals'
    repository = 'testing'
    url_name = 'pull_requests'

    username, password = get_credentials()


class PullRequestTests(TestCase):
    url_params = {'organization': SetUp.organization,
                  'repository': SetUp.repository}

    repository_url = SetUp.organization + '/' + SetUp.repository
    github = Github(SetUp.username, SetUp.password)

    def get_pr_by_title(self, pull_requests, title):
        for pr in pull_requests:
            if pr.title == title:
                return pr
        return None

    def test_analyze_pull_requests_context(self):
        url = reverse('pull_requests',
                      kwargs={'organization': SetUp.organization,
                              'repository': SetUp.repository})
        response = self.client.get(url)

        necessary_context = ('script', 'div', 'repository')
        for context in necessary_context:
            self.assertTrue(context in response.context.keys())
            self.assertIsNotNone(response.context[context])
