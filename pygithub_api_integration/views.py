from django.shortcuts import render, redirect
from github import GithubException as GE
from pygithub_api_integration.models import Repository
from pygithub_api_integration.models import Contributor
from django.contrib import messages
from django.utils.timezone import now
import socket
from . import constants


def populate_db_if_data_is_old(repo_full_name):

    DIFF_UPDATE_TIME_IN_SECONDS = 1800;
    populate = True

    repository_set = Repository.objects.filter(full_name=repo_full_name)

    if repository_set.count() > 0:
        repository = repository_set[0]
        diff_time = now() - repository.created_at
        if diff_time.total_seconds() < DIFF_UPDATE_TIME_IN_SECONDS:
            populate = False

    if populate:
        repo_request = Repository.requestRepo(repo_full_name)
        repo = Repository.saveRepo(repo_request)

        contributors_request = Contributor.requestContributors(repo_request)
        Contributor.saveContributors(contributors_request, repo)

    return Repository.objects.get(full_name=repo_full_name)

def getRepoInfo(request, organization, repository):
    repo_full_name = organization + '/' + repository

    try:

        repo = populate_db_if_data_is_old(repo_full_name)
        contributors = Contributor.objects.filter(repository=repo.id)

        context = {"repo": repo, "contributors": contributors}

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
