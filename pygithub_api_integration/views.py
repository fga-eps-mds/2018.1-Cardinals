from django.shortcuts import render, redirect
from github import GithubException as GE
from cardinals.views import getRepository
from pygithub_api_integration.models import Repository
from pygithub_api_integration.models import Contributor
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

        repo = Repository(full_name=repo_request.full_name,
                          name=repo_request.name)
        repo.save()

        for c in contributors:
            contributor = Contributor()
            contributor.id = c.author.id
            contributor.name = c.author.name
            contributor.login = c.author.login
            contributor.commits = c.total
            contributor.line_code = 0
            contributor.issues_created = 0
            contributor.issues_closed = 0
            contributor.score = 0

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
