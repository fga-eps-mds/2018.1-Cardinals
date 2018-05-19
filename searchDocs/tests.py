from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class SearchDocsTests(TestCase):

   def test_ContributingFile(self):

       organization = 'fga-gpp-mds'
       repo_name = '2018.1-Cardinals'
       repo_path = organization + '/' + repo_name

       url = reverse('renderingDocs')
       content = {'repository': repo_path}

       response = self.client.post(url, content)

       contributing = response.context['contributingFile']

       file_expected = ['CONTRIBUTING.md']
       file = [contributing.name]

       self.assertEquals(file_expected, file, True)
       self.assertNotEqual(file_expected, file, False)
    
    def test_IssueTemplate(self):

       organization = 'fga-gpp-mds'
       repo_name = '2018.1-Cardinals'
       repo_path = organization + '/' + repo_name

       url = reverse('renderingDocs')
       content = {'repository': repo_path}

       response = self.client.post(url, content)

       issuetemplate = response.context['issueTemplate']

       file_expected = ['ISSUE_TEMPLATE.md']

       file = [issuetemplate.name]

       self.assertEquals(file_expected, file)

   def test_PullRequestTemplate(self):

       organization = 'fga-gpp-mds'
       repo_name = '2018.1-Cardinals'
       repo_path = organization + '/' + repo_name

       url = reverse('renderingDocs')
       content = {'repository': repo_path}

       response = self.client.post(url, content)

       prtemplate = response.context['pullRequestTemplate']

       file_expected = ['PULL_REQUEST_TEMPLATE.md']

       file = [prtemplate.name]

       self.assertEquals(file_expected, file)

   def test_ConductFile(self):

       organization = 'fga-gpp-mds'
       repo_name = '2018.1-Cardinals'
       repo_path = organization + '/' + repo_name

       url = reverse('renderingDocs')
       content = {'repository': repo_path}

       response = self.client.post(url, content)

       conductfile = response.context['conductFile']

       file_expected = ['CODE_OF_CONDUCT.md']

       file = [conductfile.name]

       self.assertEquals(file_expected, file)

   def test_Readme(self):

       organization = 'fga-gpp-mds'
       repo_name = '2018.1-Cardinals'
       repo_path = organization + '/' + repo_name

       url = reverse('renderingDocs')
       content = {'repository': repo_path}

       response = self.client.post(url, content)

       readmefile = response.context['readme']

       file_expected = ['README.md']

       file = [readmefile.name]

       self.assertEquals(file_expected, file)
