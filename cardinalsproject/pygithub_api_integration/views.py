from django.shortcuts import render, redirect
from github import GithubException as GE
from pygithub_api_integration.models import Repository, Contributor
# from pygithub_api_integration.models import Commit
from django.contrib import messages
from . import constants
from pygithub_api_integration.updater_api import getRepoAndContributors


def getRepoInfo(request):

    repo_name = request.POST['repository']

    try:
        repo,contributors = getRepoAndContributors(repo_name)

        # commit_request = Commit.requestCommit(repo_request)
        # Commit.saveCommit(commit_request, repo, contributors)

        context = {"repo": repo, "contributors": contributors}

        return render(request, 'repository_info.html', context)
    except GE:
        messages.add_message(
            request,
            messages.ERROR,
            constants.INVALID_REPOSITORY_MESSAGE,
        )
        return redirect('index')
