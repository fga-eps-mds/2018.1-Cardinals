import requests

base_path = 'http://updater:3000'

def _create_github_url(full_name):
    url = 'https://github.com/' + full_name
    return url

class RepositoryAPI():
    contributing_file = False
    license_file = False
    issue_template = False
    pull_request_template = False
    conduct_file = False
    readme = False

    def __init__(self, organization, repository):
        repo_dict = RepositoryAPI._get_repository(organization, repository)
        self._update_docs(repo_dict)

    def _get_repository(organization, repository):
        address_repo = _create_github_url(organization + '/' + repository)
        url = base_path + '/repository/?address=' + address_repo + '&format=json'

        response = requests.get(url)
        
        response_data = response.json()
        repo_dict = response_data["Repository"]

        return repo_dict

    def _update_docs(self, repo_dict):
        self.contributing_file = repo_dict["contributing_file"]
        self.license_file = repo_dict["license_file"]
        self.issue_template = repo_dict["issue_template"]
        self.pull_request_template = repo_dict["pull_request_template"]
        self.conduct_file = repo_dict["conduct_file"]
        self.readme = repo_dict["readme"]


