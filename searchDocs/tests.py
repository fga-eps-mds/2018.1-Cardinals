from test_utils.setup_test_cases import SetupTestCases
from django.urls import reverse


class SearchDocsTests(SetupTestCases):
    url = reverse('community',
                  kwargs={'organization': SetupTestCases.organization,
                          'repository': SetupTestCases.repo_name})

    def request_file_name(self, context_name):
        response = self.client.get(SearchDocsTests.url)
        file = response.context[context_name]
        file_name = None
        if file is not None:
            file_name = file.name
        return file_name

    def assert_file_name(self, context_name, expected_name):
        response_file_name = self.request_file_name(context_name)
        self.assertEquals(response_file_name, expected_name)

    def test_repo_without_contributing_file(self):
        context_name = 'contributingFile'
        expected_name = 'CONTRIBUTING.md'
        self.assert_file_name(context_name, expected_name)

    def test_repo_with_issues_template(self):
        file_context = 'issueTemplate'
        expected_name = None
        self.assert_file_name(file_context, expected_name)

    def test_repo_with_pull_request_template(self):
        file_context = 'pullRequestTemplate'
        expected_name = None
        self.assert_file_name(file_context, expected_name)

    def test_repo_without_code_of_conduct(self):
        file_context = 'conductFile'
        expected_name = 'CODE_OF_CONDUCT.md'
        self.assert_file_name(file_context, expected_name)

    def test_repo_with_readme(self):
        file_context = 'readme'
        expected_name = None
        self.assert_file_name(file_context, expected_name)

    def test_repo_with_license(self):
        file_context = 'licenseFile'
        expected_name = None
        self.assert_file_name(file_context, expected_name)
