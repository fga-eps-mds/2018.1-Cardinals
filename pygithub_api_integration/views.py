from django.shortcuts import render
from github import Github
from index.views import searchRepository
from oauth.credentials import get_credentials


username, password = get_credentials()
repo = '2018.1-Cardinals'

'''
def getRepos(request):

    git = Github(username, password)
    user = git.get_user()
    repos = user.get_repos()

    return render(request, 'repos.html',
                  {"repos": repos})
'''


def getContributors(repo):

    contributors = repo.get_contributors()

    return contributors


def getRepoInfo(request):

    repo_name = searchRepository(request)

    git = Github()
    repo = git.get_repo(repo_name)

    contributors = getContributors(repo)
    '''
        funções que retornarão:
            os commits
            as issues
            os pull requests
            .
            .
            .
    '''

    return render(request, 'repository_info.html',
                  {"contributors": contributors})
