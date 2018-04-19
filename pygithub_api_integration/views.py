from django.shortcuts import render
from github import Github
from index.views import searchRepository
#from github import Github
# from github import GithubException

from oauth.credentials import get_credentials


username, password = get_credentials()
repo = '2018.1-Cardinals'

'''
def request_oauth_token(username, password, repo):

    try:
        git = Github(username, password)
        user = git.get_user()
        auth = user.create_authorization(scopes="public_repo", note=repo)
        return auth.token
    except GithubException as e:
        msg_error = "ERROR: " + str(e)
        return msg_error
'''

username = "mdscardinals"
password = "(cardinals1)"
#repo = '2018.1-Cardinals'

def getRepo(request):

    git = Github(username, password)
    user = git.get_user()
    repos = user.get_repos()

    return render(request, 'repos.html',
                  {"repos": repos})


def getContributors(request):

    repo_name = searchRepository(request)

    git = Github(username, password)
    repo = git.get_repo(repo_name)
    contributors = repo.get_contributors()

    return render(request, 'contributors.html',
                  {"contributors": contributors})
