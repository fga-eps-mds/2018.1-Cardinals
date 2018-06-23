from test_utils.setup_test_cases import SetupTestCases
from django.shortcuts import render, redirect, reverse
from pygithub_api_integration.models import Repository
from django.test import TestCase
#from .models import Contributor


class RankingCommitsTests(TestCase):
    organization = 'fgacardinals'
    repository = 'test_commiters'
    url_name = 'ranking_commiters'
    url = reverse(url_name,
                  kwargs={'organization': organization,
                          'repository': repository})

    def test_get_commiters_name(self):

        response = self.client.get(RankingCommitsTests.url)
        self.assertEquals(response.status_code, 200)

        commiters_context = 'ranking_commiters'
        commiters = response.context[commiters_context]
        contributors_login = [contributor.login for contributor in commiters]
        expected_logins = ['lorryaze', 'marlonbymendes']
        self.assertEquals(contributors_login, expected_logins)
