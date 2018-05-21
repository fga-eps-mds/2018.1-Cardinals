from django.urls import reverse
from django.test import TestCase

class SetupTestCases(TestCase):
    organization = 'fga-gpp-mds'
    repo_name = '2018.1-Cardinals'
    repo_path = organization + '/' + repo_name

    def make_client_request(self, url_name, repo_path = None):
        url = reverse(url_name)

        if repo_path is None:
            repo_path = SetupTestCases.repo_path

        content = {'repository': repo_path}
        response = self.client.post(url, content)
        return response

    def debug_response(self, response):
        print('\n' * 3)
        print('-> Debugging response started')
        print('response.content = {}'.format(response.content))
        print('response.status_code = {}'.format(response.status_code))
        print('-> Debugging response finished')
