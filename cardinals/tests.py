from django.test import TestCase
from django.urls import reverse
from oauth.credentials import get_credentials

from github import Github

from .views import *


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

    def test_pull_request_opened_time_for_closed_pr(self):
        repository = PullRequestTests.github.\
            get_repo(PullRequestTests.repository_url)

        pull_requests = repository.get_pulls(state='all')

        expected_pr_title = 'Auto commit: GfftEZeNfuW'
        expected_opened_time = 3

        pr = self.get_pr_by_title(pull_requests, expected_pr_title)
        opened_time = get_pull_request_opened_time(pr).days

        self.assertEquals(pr.title, expected_pr_title)
        self.assertEquals(opened_time, expected_opened_time)

    def test_pull_request_opened_time_for_opened_pr(self):
        repository = PullRequestTests.github.\
            get_repo(PullRequestTests.repository_url)

        pull_requests = repository.get_pulls(state='all')

        expected_pr_title = 'Auto commit: peDBFQDrihx'
        expected_opened_time = 0

        pr = self.get_pr_by_title(pull_requests, expected_pr_title)
        opened_time = get_pull_request_opened_time(pr).days

        self.assertEquals(pr.title, expected_pr_title)
        self.assertIsNone(pr.closed_at)
        self.assertTrue(opened_time >= expected_opened_time)

    def test_get_pull_requests_opened_time(self):
        repository = PullRequestTests.github.\
            get_repo(PullRequestTests.repository_url)

        pull_requests = repository.get_pulls(state='all')

        closed_pr_title = 'Auto commit: GfftEZeNfuW'
        closed_pr_expected_opened_time = 3

        still_opened_pr_title = 'Auto commit: peDBFQDrihx'

        prs_opened_time = get_pull_requests_opened_time(pull_requests)
        for index, pr in enumerate(pull_requests):
            opened_time = prs_opened_time[index].days
            if pr.title == closed_pr_title:
                self.assertEquals(opened_time, closed_pr_expected_opened_time)
            elif pr.title == still_opened_pr_title:
                self.assertTrue(opened_time >= 0)

    def test_get_opened_time_xy_axis(self):
        repository = PullRequestTests.github.\
            get_repo(PullRequestTests.repository_url)

        pull_requests = repository.get_pulls(state='all')
        prs_opened_time = get_pull_requests_opened_time(pull_requests)

        x, y = get_opened_time_xy_axis(prs_opened_time)

        expected_y = [1, 1]
        self.assertEquals(y, expected_y)

        self.assertEquals(x[0], 3)
        self.assertTrue(x[1] >= 0)