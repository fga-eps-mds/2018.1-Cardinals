from django.shortcuts import render, redirect
from github import GithubException as GE
from cardinals.views import getRepository
from pygithub_api_integration.models import Repository
from pygithub_api_integration.models import Contributor
from pygithub_api_integration.models import Issue
from django.contrib import messages
from . import constants


def getRepoInfo(request):

    repo_name = getRepository(request)

    try:
        repo_request = Repository.requestRepo(repo_name)
        repo = Repository.saveRepo(repo_request)

        contributors_request = Contributor.requestContributors(repo_request)
        Contributor.saveContributors(contributors_request, repo)

        issue_request = Issue.requestIssues(repo_request)
        Issue.saveIssues(issue_request, repo)

        contributors = Contributor.objects.filter(repository=repo.id)

        context = {"repo": repo, "contributors": contributors}

        return render(request, 'repository_info.html', context)

    except GE:
        messages.add_message(
            request,
            messages.ERROR,
            constants.INVALID_REPOSITORY_MESSAGE,
        )
        return redirect('index')
