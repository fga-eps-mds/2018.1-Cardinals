from django.shortcuts import render, redirect
from github import GithubException as GE
from cardinals.views import getRepository
from pygithub_api_integration.models import Repository
from pygithub_api_integration.models import Contributor
from pygithub_api_integration.models import Issue
from django.contrib import messages
from . import constants


def getContributors(repo):

    contributors = repo.get_stats_contributors()

    return contributors


def getRepoInfo(request):

    repo_name = getRepository(request)

    try:
        repo_request = Repository.requestRepo(repo_name)
        contributors = getContributors(repo_request)

        repo = Repository()
        repo.full_name = repo_request.full_name
        repo.name = repo_request.name

        repo.save()

        Issue.requestIssues(repo_request, repo)

        for c in contributors:
            contributor = Contributor()
            contributor.id = c.author.id
            contributor.name = c.author.name
            contributor.login = c.author.login
            contributor.commits = c.total

            contributor.save()
            contributor.repository.add(repo)

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
