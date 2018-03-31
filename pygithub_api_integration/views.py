from django.shortcuts import render
# from django.http import HttpResponse
from github import Github


def getPygithub(request):
    git = Github("Mateusas3s", "123qaz.;/")
    git = Github("9a9d59fc51a9f25ade73f785214ba0f935749ee6")
    user = git.get_user()
    repos = user.get_repos()

    return render(request, 'repos.html',
                  {"repos": repos})


def getContributors(request):

    git = Github("9a9d59fc51a9f25ade73f785214ba0f935749ee6")
    org = git.get_organization('fga-gpp-mds')
    repo = org.get_repo('2018.1-Cardinals')
    contributors = repo.get_contributors()
    return render(request, 'contributors.html',
                  {"contributors": contributors})
