from test_utils.setup_test_cases import SetupTestCases
from django.shortcuts import render, redirect, reverse
from pygithub_api_integration.models import Repository
from django.test import TestCase
#from .models import Contributor


class RankingCommitsTests(SetupTestCases):

    def test_get_commiters_name(self):
        url = reverse('pull_requests',
                      kwargs={'organization': SetupTestCases.organization,
                              'repository': SetupTestCases.repo_name})
        response = self.client.get(url)

        print("TESTE")
        print(response)