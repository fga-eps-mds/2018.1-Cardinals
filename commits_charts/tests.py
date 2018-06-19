from django.test import TestCase
from django.urls import reverse
from oauth.credentials import get_credentials
from github import Github, Commit

from .views import (analyze_commits_charts,)


class SetUp:
    organization = 'fgacardinals'
    repository = 'testing'
    url_name = 'commits_charts'
    username, password = get_credentials()


class CommitsTests(TestCase):
    url_params = {'organization': SetUp.organization,
                  'repository': SetUp.repository}
    repository_url = SetUp.organization + '/' + SetUp.repository
    github = Github(SetUp.username, SetUp.password)

    def get_commit_by_sha(self, commits_charts, sha):
        for pr in commits_charts:
            if pr.sha == sha:
                return pr
        return None

    def test_analyze_commits_charts_context(self):
        url = reverse('commits_charts',
                      kwargs={'organization': SetUp.organization,
                              'repository': SetUp.repository})
        response = self.client.get(url)
        necessary_context = ('script', 'div', 'repository')
        for context in necessary_context:
            self.assertTrue(context in response.context.keys())
            self.assertIsNotNone(response.context[context])


