from test_utils.setup_test_cases import SetupTestCases
from django.test import TestCase
from .models import Contributor
# from . import constants


class RepoInfoTests(SetupTestCases):

    url_name = 'getRepoInfo'

    def test_get_repo_name(self):
        response = self.make_client_request(RepoInfoTests.url_name)
        response_repo_name = response.context['repo'].name

        self.assertEquals(SetupTestCases .repo_name, response_repo_name)

    def test_get_contributors_name(self):
        response = self.make_client_request(RepoInfoTests.url_name)

        contributors = response.context['contributors']

        contributors_name_expected = ['Amanda Bezerra',
                                      'Mateus Augusto Sousa e Silva',
                                      'Marlon Mendes', 'Guilherme da Luz',
                                      'Lucas Costa', 'Gustavo Duarte Moreira',
                                      'Matheus Gomes', 'Lorrany Azevedo',
                                      'João Pedro', 'Mik', 'Victor Moura']

        contributors_name_expected = set(contributors_name_expected)

        contributors_name = set([c.name for c in contributors])

        self.assertEquals(contributors_name, contributors_name_expected)

    def test_get_contributors_login(self):
        response = self.make_client_request(RepoInfoTests.url_name)

        contributors = response.context['contributors']

        contributors_login_expected = ['amandabezerra', 'Mateusas3s',
                                       'marlonbymendes', 'daluzguilherme',
                                       'gustavoduartemoreira', 'matheusgomesf',
                                       'jpmartins201', 'lorryaze',
                                       'lucasca73', 'victorcmoura',
                                       'MiguelNery']

        contributors_login_expected = set(contributors_login_expected)

        contributors_login = set([c.login for c in contributors])

        self.assertEquals(contributors_login, contributors_login_expected)

    # def test_invalid_repository_name(self):
    #     string_temp = 'just/a/long/url/to/' + 'make/sure/it/is/not/'
    #     string_temp2 = 'found/on/github/dot/com/9817231285103'
    #     invalid_repo_path = string_temp + string_temp2
    #     response = self.make_client_request(RepoInfoTests.url_name,
    #                                         invalid_repo_path)

    #     messages = [m.message for m in response.context['messages']]

    #     self.assertTrue(constants.INVALID_REPOSITORY_MESSAGE in messages)


class ModelContributorsTest(TestCase):

    def setUp(self):

        self.contributors = []

        for i in range(10):
            self.contributors.append(Contributor(id=1,
                                                 name='Warnoldison',
                                                 login='warnoldison@gmail.com',
                                                 commits=10,
                                                 line_code=100,
                                                 issues_created=10,
                                                 issues_closed=10,
                                                 score=40))

    def testGetLineCodeRepo(self):

        self.assertEquals(Contributor.getLineCodeRepo(self.contributors), 1000)

    def testGetPercent(self):

        for c in self.contributors:
            self.assertEquals(Contributor.getPercent(c.line_code, 1000), 10)
