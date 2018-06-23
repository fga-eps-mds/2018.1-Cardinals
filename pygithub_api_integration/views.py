from django.shortcuts import render, redirect
from github import GithubException as GE
from pygithub_api_integration.models import Repository
from pygithub_api_integration.models import Contributor
from django.contrib import messages
import socket
from . import constants
from cardinals.views import *


def get_repo_info(request, organization, repository):
    repo_name = organization + '/' + repository

    try:

        repo_request = Repository.requestRepo(repo_name)
        repo = Repository.saveRepo(repo_request)

        contributors_request = Contributor.requestContributors(repo_request)
        Contributor.saveContributors(contributors_request, repo)

        contributors = Contributor.objects.filter(repository=repo.id)

        analyze_commits_charts(request, organization, repository, 500, 350)
        div = divCommit()
        script = scriptCommit()

        context = {"repo": repo, "contributors": contributors, "div": div, "script": script}

        return render(request, 'repository_info.html', context)

    except socket.timeout and socket.gaierror:
        messages.add_message(
            request,
            messages.ERROR,
            constants.TIMEOUT_MESSAGE,
        )

    except GE:
        messages.add_message(
            request,
            messages.ERROR,
            constants.INVALID_REPOSITORY_MESSAGE,
        )

        return redirect('index')

