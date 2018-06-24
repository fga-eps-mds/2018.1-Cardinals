from django.shortcuts import render
from django.shortcuts import HttpResponse

def loginGithub(request, organization, repository):
    organization = 'fgacardinals'
    repository  = 'test_commiters'
    path_name= organization + '/' + repository

    return HttpResponse("Login Github APP")