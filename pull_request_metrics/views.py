from django.shortcuts import render
from django.http import HttpResponse
from oauth.credentials import get_credentials

username, password = get_credentials()


def analyze_pull_requests(request, organization, repository):
    out = 'organization = {}<br>'.format(organization)
    out += 'repository = {}<br>'.format(repository)

    return HttpResponse(out)
