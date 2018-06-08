from django.shortcuts import render, redirect
from github import GithubException as GE
from cardinals.views import getRepository
from pygithub_api_integration.models import Repository
from pygithub_api_integration.models import Contributor
# from pygithub_api_integration.models import Commit
from django.contrib import messages
from . import constants


def save_repository_name_in_session(request, repo_name):
    request.session['repository'] = repo_name


def getRepoInfo(request):
    repo_name = getRepository(request)
    save_repository_name_in_session(request, repo_name)

    try:
        repo_request = Repository.requestRepo(repo_name)
        repo = Repository.saveRepo(repo_request)

        contributors_request = Contributor.requestContributors(repo_request)
        Contributor.saveContributors(contributors_request, repo)

        contributors = Contributor.objects.filter(repository=repo.id)

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
