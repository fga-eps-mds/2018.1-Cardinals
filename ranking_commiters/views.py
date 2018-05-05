from django.shortcuts import render
from github import Github
from oauth.credentials import get_credentials

username, password = get_credentials()

g = Github(username, password)
org = g.get_organization('fga-gpp-mds')
repo = org.get_repo('2018.1-Cardinals')


def rankingCommiters(request):

    commits_user = repo.get_stats_contributors()

    return render(request, 'rankingCommiters.html',
                  {"commits_user": commits_user})
