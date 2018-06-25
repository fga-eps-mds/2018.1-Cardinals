from test_utils.setup_test_cases import SetupTestCases
from django.test import TestCase
from .models import Contributor
# from . import constants


class RepoInfoTests(SetupTestCases):

    url_name = SetupTestCases.organization + '/' + SetupTestCases.repo_name

    def setUp(self):
        response = self.make_client_request(RepoInfoTests.url_name)
        self.contributors = response.context['contributors']

    def test_get_repo_name(self):
        response = self.make_client_request(RepoInfoTests.url_name)
        response_repo_name = response.context['repo'].name

        self.assertEquals(SetupTestCases .repo_name, response_repo_name)

    def test_get_contributors_name(self):

        contributors_name_expected = ['Marlon Mendes']

        contributors_name_expected = set(contributors_name_expected)

        contributors_name = set([c.name for c in self.contributors])

        self.assertEquals(contributors_name, contributors_name_expected)

    def test_get_contributors_login(self):

        contributors_login_expected = ['marlonbymendes']

        contributors_login_expected = set(contributors_login_expected)

        contributors_login = set([c.login for c in self.contributors])

        self.assertEquals(contributors_login, contributors_login_expected)


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
