from django.shortcuts import render
from github import Github


class GithubSingleton:
    _github = None

    def __init__(self):
        pass

    def __set_github(self, request):
        token = get_access_token(request)
        self._github = Github(token)
        return self._github

    def get_github(self, request):
        assert request.user.is_authenticated

        if self._github:
            return self._github
        else:
            return self.__set_github(request)


github_singleton = GithubSingleton()


def get_access_token(request):
    user = request.user
    social = user.social_auth.get(provider='github')
    access_token = social.extra_data['access_token']
    return access_token


def home(request):

    context = {}
    if request.user.is_authenticated:
        g = github_singleton.get_github(request)
        user = g.get_user()
        repo_names = [(repo.full_name, repo.html_url)
                      for repo in user.get_repos(type='all')]

        orgs = user.get_orgs()
        orgs_names = [(org.login, org.html_url) for org in orgs]

        context = {'repositories': repo_names,
                   'organizations': orgs_names}

    return render(request, 'home_login.html', context=context)
