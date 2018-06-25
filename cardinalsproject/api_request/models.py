import requests
from datetime import datetime
from ranking_commiters.models import Weight

base_path = 'http://updater:3000'

def _create_github_url(full_name):
    url = '?address=https://github.com/' + full_name + '&format=json'
    return url

def _get_api_reponse(api_url , organization, repository):
        address_repo = _create_github_url(organization + '/' + repository)
        url = base_path + api_url + address_repo

        response = requests.get(url)
        response_data = response.json()
        
        return response_data

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

        response = _get_api_reponse("/repository/" ,organization ,repository)

        self._update_docs(response["Repository"])
        self._update_repository(response["Repository"])
        self._update_contributors(response["Contributors"])

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

    def update_score(self, weight=None):
        for c in self.contributors:
            c.update_score(weight)

# private class for repository use
class _RepositoryContributorAPI():
    def __init__(self, repo_dict):
        self.name = repo_dict["name"]
        self.login = repo_dict["login"]
        self.commits = repo_dict["commits"]
        self.line_code = repo_dict["line_code"]
        self.issues_created = repo_dict["issues_created"]
        self.issues_closed = repo_dict["issues_closed"]
        self.score = 0

    def update_score(self, weight=None):
        p1 = 1
        p2 = 1
        p3 = 1
        p4 = 1

        if weight is not None:
            p1 = weight.commit
            p2 = weight.line_code
            p3 = weight.issues_created
            p4 = weight.issues_closed

        self.score = self.commits*p1 + self.line_code*p2 + self.issues_created*p3 + self.issues_closed*p4



class CommitsChartAPI():

    def __init__(self, organization, repository):
        self.paired = []
        self.commits = []
        self.dates = []

        reponse = _get_api_reponse("/repository/commits_pair_chart_data/" ,organization ,repository)
        self._update_chart_data(reponse)
        pass

    def _update_chart_data(self, response_data):

        self.commits = response_data["commits"]
        self.paired = response_data["paired"]

        for dt in response_data["dates"]:
            py_date = datetime.strptime(dt, '%d-%m-%Y')
            self.dates.append(py_date)
        
        self.dates.sort()

class RequestIssuesAPI():
    def __init__(self, organization, repository):

        self.issues = []

        response = _get_api_reponse("/repository/issues/" ,organization ,repository)

        for issue_dict in response["Issues"]:
            issue = IssueAPI(issue_dict)
            self.issues.append(issue)
        pass


class IssueAPI():
    def __init__(self, issue_dict):

        # 2018-06-25T01:00:00
        date_regex = '%Y-%m-%dT%H:%M:%S'

        self.created_date = datetime.strptime( issue_dict['created_at'], date_regex)

        if issue_dict['state'] == 'open':
            self.closed_date = datetime.now()
        else:
            self.closed_date = datetime.strptime( issue_dict['closed_at'], date_regex)

        self.duration = (self.closed_date - self.created_date).days

class RequestPullRequest():
    def __init__(self, organization, repository):

        self.pulls = []

        response = _get_api_reponse("/repository/pulls/" ,organization ,repository)

        for pull in response["PullRequests"]:
            pr = PullRequestAPI(pull)
            self.pulls.append(pr)
        pass


class PullRequestAPI():
    def __init__(self, pr_dict):

        # 2018-06-25T01:00:00
        date_regex = '%Y-%m-%dT%H:%M:%S'

        self.created_date = datetime.strptime( pr_dict['created_at'], date_regex)

        if pr_dict['state'] == 'open':
            self.closed_date = datetime.now()
        else:
            self.closed_date = datetime.strptime( pr_dict['closed_at'], date_regex)

        self.duration = (self.closed_date - self.created_date).days
