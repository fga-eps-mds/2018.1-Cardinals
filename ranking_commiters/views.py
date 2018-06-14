from django.shortcuts import render
from operator import attrgetter
from pygithub_api_integration.models import Contributor
from pygithub_api_integration.models import Repository
from pygithub_api_integration.models import Issue
from ranking_commiters.models import Weight


def getResult(request, organization, repository):

    repo_name = organization + '/' + repository

    if request.method == 'GET':

        repo_request = Repository.requestRepo(repo_name)
        repo = Repository.saveRepo(repo_request)

        issue_request = Issue.requestIssues(repo_request)
        Issue.saveIssues(issue_request, repo)

        commiters = Contributor.objects.filter(repository=repo.id)

        Contributor.setLineCodeContrib(commiters)
        Contributor.setIssuesCreatedFor(commiters, repo_name)
        Contributor.setIssuesClosedFor(commiters, repo_name)

        commiters = Contributor.getScore(commiters)

    elif request.method == 'POST':

        commiters = Contributor.objects.filter(repository=repo_name)

        weight = Weight.requestWeight(request)

        commiters = Contributor.getScore(commiters, weight=weight)

    ranking_commiters = sorted(commiters,
                               key=attrgetter('score'),
                               reverse=True)

    context = {"repo_id": repo_name, "ranking_commiters": ranking_commiters}

    return render(request, 'rankingCommiters.html', context)
