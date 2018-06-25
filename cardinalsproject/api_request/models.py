import requests
from datetime import datetime

base_path = 'http://updater:3000'

def _create_github_url(full_name):
    url = 'https://github.com/' + full_name + '&format=json'
    return url

class RepositoryAPI():
    
    def __init__(self, organization, repository):

        self.contributors = []
        self.name = ""
        self.full_name = ""

        self.contributing_file = False
        self.license_file = False
        self.issue_template = False
        self.pull_request_template = False
        self.conduct_file = False
        self.readme = False

        response = RepositoryAPI._get_response(organization, repository)

        self._update_docs(response["Repository"])
        self._update_repository(response["Repository"])
        self._update_contributors(response["Contributors"])

    def _get_response(organization, repository):
        address_repo = _create_github_url(organization + '/' + repository)
        url = base_path + '/repository/?address=' + address_repo

        response = requests.get(url)
        response_data = response.json()

        return response_data

    def _update_docs(self, repo_dict):
        self.contributing_file = repo_dict["contributing_file"]
        self.license_file = repo_dict["license_file"]
        self.issue_template = repo_dict["issue_template"]
        self.pull_request_template = repo_dict["pull_request_template"]
        self.conduct_file = repo_dict["conduct_file"]
        self.readme = repo_dict["readme"]

    def _update_contributors(self, repo_dict):
        for contrib in repo_dict:
            new_contrib = _RepositoryContributorAPI(contrib)
            self.contributors.append(new_contrib)
        pass

    def _update_repository(self, repo_dict):
        self.name = repo_dict["name"]
        self.full_name = repo_dict["full_name"]
        pass

# private class for repository use
class _RepositoryContributorAPI():
    def __init__(self, repo_dict):
        self.name = repo_dict["name"]
        self.login = repo_dict["login"]
        self.commits = repo_dict["commits"]


class CommitsChartAPI():

    def __init__(self, organization, repository):
        self.paired = []
        self.commits = []
        self.dates = []

        reponse = self._get_commit_chart_reponse(organization, repository)
        self._update_chart_data(reponse)
        pass

    def _get_commit_chart_reponse(self, organization, repository):
        address_repo = _create_github_url(organization + '/' + repository)
        url = base_path + '/repository/commits_pair_chart_data/?address=' + address_repo

        response = requests.get(url)
        response_data = response.json()
        
        return response_data


    def _update_chart_data(self, response_data):

        self.commits = response_data["commits"]
        self.paired = response_data["paired"]

        for dt in response_data["dates"]:
            py_date = datetime.strptime(dt, '%d-%m-%Y')
            self.dates.append(py_date)
        
        self.dates.sort()

