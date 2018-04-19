from django.shortcuts import render
from github import Github


def getContributors(request):

    repo = 'fga-gpp-mds/2018.1-Cardinals'

    git = Github()
    repo = git.get_repo(repo)
    contributors = repo.get_contributors()

    return render(request, 'contributors.html',
                  {"contributors": contributors})
