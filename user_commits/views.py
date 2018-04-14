from github import Github
from django.shortcuts import render
from index.views import searchRepository
from oauth.credentials import get_credentials
from datetime import datetime


username, password = get_credentials()
repo = '2018.1-Cardinals'


def user_commits(request):
    allCommits = repo.get_stats_contributors()
    return allCommits


def getRepoInfo(request):

    repo_name = searchRepository(request)

    git = Github()
    repo = git.get_repo(repo_name)

    allcommits = getAllCommits(repo)
    
    return render(request, 'user_commits.html',
                  {"allcommits ": allcommits})
