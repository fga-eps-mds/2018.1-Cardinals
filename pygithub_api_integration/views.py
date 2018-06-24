from django.shortcuts import render, redirect
from github import GithubException as GE
from pygithub_api_integration.models import Repository
from pygithub_api_integration.models import Contributor
from django.contrib import messages
from datetime import datetime, timedelta
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

        analyze_commits_charts(request, organization, repository, 1000, 400)
        analyze_issue_graph(request, organization, repository)
        analyze_pull_requests(request, organization, repository)

        div = divCommit()
        script = scriptCommit()

        div2 = divIssue()
        script2 = scriptIssue()

        divPR = divRequest()
        scriptPR = scriptRequest()

        context = {"repo": repo, "contributors": contributors,
                   "div": div, "script": script,
                   "divPR": divPR, "scriptPR": scriptPR,
                   "div2": div2, "script2": script2}

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

