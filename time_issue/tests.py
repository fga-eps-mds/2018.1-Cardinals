from django.test import TestCase
from django.urls import reverse
from oauth.credentials import get_credentials
from github import Github, Issue

from .views import (analyze_issue_graph,)


class SetUp:
    organization = 'fgacardinals'
    repository = 'testing'
    url_name = 'time_issue'
    username, password = get_credentials()


class IssuesTests(TestCase):
    url_params = {'organization': SetUp.organization,
                  'repository': SetUp.repository}
    repository_url = SetUp.organization + '/' + SetUp.repository
    github = Github(SetUp.username, SetUp.password)

    def get_issue_by_id(self, time_issue, id):
        for issue_id in time_issue:
            if issue_id.id == id:
                return issue_id
        return None

    def test_analyze_issue_graph_context(self):
        url = reverse('time_issue',
                      kwargs={'organization': SetUp.organization,
                              'repository': SetUp.repository})
        response = self.client.get(url)
        necessary_context = ('script', 'div', 'repository')
        for context in necessary_context:
            self.assertTrue(context in response.context.keys())
            self.assertIsNotNone(response.context[context])
