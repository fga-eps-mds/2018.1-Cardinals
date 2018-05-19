from django.test import TestCase
from django.urls import reverse

from . import constants


class RepoInfoTests(TestCase):
    organization = 'fga-gpp-mds'
    repo_name = '2018.1-Cardinals'
    repo_path = organization + '/' + repo_name

    def make_client_request(self, repo_path = None):
        url = reverse('getRepoInfo')

        if repo_path is None:
            repo_path = RepoInfoTests.repo_path

        content = {'repository': repo_path}
        response = self.client.post(url, content)
        return response


    def test_get_repo_name(self):
        response = self.make_client_request()
        response_repo_name = response.context['repo'].name

        self.assertEquals(RepoInfoTests.repo_name, response_repo_name)


    def test_get_contributors_name(self):
        response = self.make_client_request()

        contributors = response.context['contributors']

        contributors_name_expected = ['Amanda Bezerra', 'Mateus Augusto Sousa e Silva', 'Marlon Mendes', 'Guilherme da Luz',
                                      'Lucas Costa', 'Gustavo Duarte Moreira', 'Matheus Gomes', 'Lorrany Azevedo',
                                      'João Pedro', 'Mik', 'Victor Moura' ]

        contributors_name_expected = set(contributors_name_expected)

        contributors_name = set([contributor.name for contributor in contributors])

        self.assertEquals(contributors_name, contributors_name_expected)


    def test_get_contributors_login(self):
        response =  self.make_client_request()

        contributors =  response.context['contributors']

        contributors_login_expected = ['amandabezerra', 'Mateusas3s', 'marlonbymendes', 'daluzguilherme',
                                       'gustavoduartemoreira', 'matheusgomesf', 'jpmartins201', 'lorryaze',
                                       'lucasca73', 'victorcmoura', 'MiguelNery']

        contributors_login_expected = set(contributors_login_expected)

        contributors_login = set([contributor.login for contributor in contributors])

        self.assertEquals(contributors_login, contributors_login_expected)

    def test_invalid_repository_name(self):
        invalid_repo_path = 'just/a/long/url/to/make/sure/it/is/not/found/on/github/dot/com/9817231285103'
        response = self.make_client_request(invalid_repo_path)

        messages = [message.message for message in response.context['messages']]

        self.assertTrue(constants.INVALID_REPOSITORY_MESSAGE in messages)
