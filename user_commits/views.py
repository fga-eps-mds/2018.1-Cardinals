from github import Github
from django.shortcuts import render
from index.views import searchRepository
from oauth.credentials import get_credentials
from datetime import datetime


def getCommitsUser(repo):

    commits_user = repo.get_stats_contributors()

    return commits_user

def getCommitStatuses(repo):

    commit_statuses = repo.get_commits()

    return commit_statuses


def getCommits(request):

    username, password = get_credentials()
    repo_name = ('fga-gpp-mds/2018.1-Cardinals')
    #repo_name = searchRepository(request)

    git = Github(username, password)
    repo = git.get_repo(repo_name)

    commits_user = getCommitsUser(repo)
    commit_statuses = getCommitStatuses(repo)
    
    return render(request, 'user_commits.html',{"commits_user": commits_user, "commit_statuses": commit_statuses})