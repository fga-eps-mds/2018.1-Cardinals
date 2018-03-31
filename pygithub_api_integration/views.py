# from django.shortcuts import render
from django.http import HttpResponse
from github import Github


def getPygithub(request):
    # First create a Github instance:

    # using username and password
    g = Github("Mateusas3s", "123qaz.;/")

    # or using an access token
    g = Github("9a9d59fc51a9f25ade73f785214ba0f935749ee6")

    # Then play with your Github objects:
    for repo in g.get_user().get_repos():
        return HttpResponse(repo.name + '</br>')
