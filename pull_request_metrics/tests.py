from django.test import TestCase
from django.urls import reverse
from oauth.credentials import get_credentials

from github import Github, PaginatedList, PullRequest

# Create your tests here.

from .views import get_pull_request_opened_time

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

    def get_pr_by_title(self,  pull_requests, title):
        for pr in pull_requests:
            if pr.title == title:
                return pr
        return None

    def test_pull_request_opened_time(self):
        repository = PullRequestTests.github.get_repo(PullRequestTests.repository_url)

        pull_requests = repository.get_pulls(state='all')

        expected_pr_title = 'Auto commit: GfftEZeNfuW'
        expected_opened_time = 3

        pr = self.get_pr_by_title(pull_requests, expected_pr_title)
        opened_time = get_pull_request_opened_time(pr).days

        self.assertEquals(pr.title, expected_pr_title)
        self.assertEquals(opened_time, expected_opened_time)
