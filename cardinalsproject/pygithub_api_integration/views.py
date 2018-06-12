from django.shortcuts import render, redirect
from github import GithubException as GE
from pygithub_api_integration.models import Repository, Contributor
# from pygithub_api_integration.models import Commit
from django.contrib import messages
from . import constants
from pygithub_api_integration.updater_api import getAsyncRepoId


def getRepoInfo(request):

    repo_name = request.POST['repository']

    # repo_name = getRepository(request)

    try:
        # repo_request = Repository.requestRepo(repo_name)
        # repo = Repository.saveRepo(repo_request)

        # contributors_request = Contributor.requestContributors(repo_request)
        # Contributor.saveContributors(contributors_request, repo)

        repo_id = getAsyncRepoId(repo_name)

        if( repo_id is not None ):

            repo = Repository.objects.filter(id=repo_id)
            contributors = Contributor.objects.filter(repository=repo_id)

            # commit_request = Commit.requestCommit(repo_request)
            # Commit.saveCommit(commit_request, repo, contributors)

            context = {"repo": repo, "contributors": contributors}

            return render(request, 'repository_info.html', context)
        else:
            return redirect('index')
        

    except GE:
        messages.add_message(
            request,
            messages.ERROR,
            constants.INVALID_REPOSITORY_MESSAGE,
        )
        return redirect('index')
