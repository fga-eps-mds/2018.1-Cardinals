from django.shortcuts import render
from github import Github


class GithubSingleton:
    _github = None

    def __init__(self):
        pass

    def __set_github(self, request):
        token = get_access_token(request)
        GithubSingleton._github = Github(token)
        return GithubSingleton._github

    def get_github(self, request):
        assert request.user.is_authenticated

        if GithubSingleton._github:
            return GithubSingleton._github
        else:
            return self.__set_github(request)


github_singleton = GithubSingleton()


def get_access_token(request):
    user = request.user
    social = user.social_auth.get(provider='github')
    access_token = social.extra_data['access_token']
    return access_token


def save_organizations_in_session(request, orgs):
    data = dict()

    for org in orgs:
        repos = org.get_repos(type='all')
        repo_names = [repo.full_name for repo in repos]
        data[org.login] = repo_names

    request.session['organizations'] = data


def home(request):

    context = {}
    if request.user.is_authenticated:
        g = github_singleton.get_github(request)
        user = g.get_user()

        repo_names = [repo.full_name
                      for repo in user.get_repos(type='all')]


        orgs = user.get_orgs()
        save_organizations_in_session(request, orgs)

        orgs_logins = [org.login for org in orgs]

        context = {'repositories': repo_names,
                   'organizations': orgs_logins}

    return render(request, 'home_login.html', context=context)

def get_repos_from_organization(request, login):
    organizations = request.session.get('organizations', None)
    repositories = organizations.get(login, None)
    return repositories

def organization(request, login):
    print('Im inside organization')
    repositories = get_repos_from_organization(request, login)
    context = {'login': login,
               'repositories': repositories}
    return render(request, 'organizations.html', context=context)
