from django.urls import reverse
from django.test import TestCase


class SetupTestCases(TestCase):
    organization = 'fgacardinals'
    repo_name = 'testing'
    repo_path = organization + '/' + repo_name

    def make_client_request(self, repo_path=None):

        kwargs = {'organization': SetupTestCases.organization,
                  'repository': SetupTestCases.repo_name}

        url = reverse('get_repo_info', kwargs=kwargs)

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
