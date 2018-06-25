from test_utils.setup_test_cases import SetupTestCases
from django.shortcuts import render, redirect, reverse
from django.test import TestCase


class RankingCommitsTests(TestCase):
    organization = 'fgacardinals'
    repository = 'test_commiters'
    url_name = 'ranking_commiters'

    url = reverse(url_name,
                  kwargs={'organization': organization,
                          'repository': repository})
    url_info = reverse('get_repo_info',
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

    def test_ranking_commiters_with_user_weights(self):
        weights = {
                    'weight_commit': 3,
                    'weight_line_code': 2,
                    'weight_issues_created': 5,
                    'weight_issues_closed': 10,
                  }
        contributors = ('lorryaze', 'marlonbymendes')

        response = self.client.post(RankingCommitsTests.url, weights)
        self.assertEquals(response.status_code, 200)

        commiters_context = 'ranking_commiters'
        commiters = response.context[commiters_context]

        score = dict()
        for commiter in commiters:
            score[commiter.login] = commiter.score

        print('score = {}'.format(score))

        self.assertTrue(score[contributors[0]] >= score[contributors[1]])
