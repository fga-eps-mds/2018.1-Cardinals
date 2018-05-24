from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from oauth.credentials import get_credentials

from github import Github
from github import GithubException as GE

username, password = get_credentials()


def analyze_pull_requests(request, organization, repository):

    repository_url = organization + '/' + repository
    github = Github(username, password)
    github_repository = github.get_repo(repository_url)
    github_pull_requests = github_repository.get_pulls()

    out = '<h1> Pull requests<h1><br>'
    for pr in github_pull_requests:
        out += (pr.title + ' ')

        time_open = pr.created_at
        time_close = pr.closed_at

        if time_close is None:
            time_close = datetime.now()

        metric_time = (time_close - time_open)
        out += str(metric_time) + '<br>'

    return HttpResponse(metric_time)
