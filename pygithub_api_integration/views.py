from django.shortcuts import render
from github import Github
from index.views import searchRepository
from oauth.credentials import get_credentials


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

def getCommitsUser(repo):

    commits_user = repo.get_stats_contributors()

    return commits_user


def getRepoInfo(request):

    username, password = get_credentials()

    repo_name = searchRepository(request)

    git = Github(username, password)
    repo = git.get_repo(repo_name)

    contributors = getContributors(repo)

    commits_user = getCommitsUser(repo)
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
                  {"contributors": contributors,
                   "commits_user": commits_user})
