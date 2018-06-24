from django.shortcuts import render
from pygithub_api_integration.models import Contributor
from pygithub_api_integration.models import Repository
from pygithub_api_integration.models import Issue
from ranking_commiters.models import Weight


def ranking_commiters(request, organization, repository):

    name = organization + '/' + repository
    repo = Repository.objects.get(full_name=name)
    repo_id = repo.id

    repo = Repository.objects.get(id=repo_id)
    commiters = Contributor.objects.filter(repository=repo_id)

    if request.method == 'GET':

        repo_request = Repository.requestRepo(repo.full_name)

        issue_request = Issue.requestIssues(repo_request)
        Issue.saveIssues(issue_request, repo)

        Contributor.setLineCodeContrib(commiters)
        Contributor.setIssuesCreatedFor(commiters, repo_id)
        Contributor.setIssuesClosedFor(commiters, repo_id)

        ranking_commiters = Contributor.getScore(commiters)

    elif request.method == 'POST':

        weight = Weight.requestWeight(request, repo)

        ranking_commiters = Contributor.getScore(commiters, weight=weight)

    context = {"repo_id": repo_id, "ranking_commiters": ranking_commiters}

    return render(request, 'rankingCommiters.html', context)
