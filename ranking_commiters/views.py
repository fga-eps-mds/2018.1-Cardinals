from django.shortcuts import render
from operator import attrgetter
from pygithub_api_integration.models import Contributor
from ranking_commiters.models import Weight


def getResult(request, repo_id):

    commiters = Contributor.objects.filter(repository=repo_id)

    if request.method == 'GET':

        Contributor.setLineCodeContrib(commiters)
        Contributor.setIssuesCreatedFor(commiters, repo_id)
        Contributor.setIssuesClosedFor(commiters, repo_id)

        commiters = Contributor.getScore(commiters)

    elif request.method == 'POST':

        weight = Weight.requestWeight(request)

        commiters = Contributor.getScore(commiters, weight=weight)

    ranking_commiters = sorted(commiters,
                               key=attrgetter('score'),
                               reverse=True)

    context = {"repo_id": repo_id, "ranking_commiters": ranking_commiters}

    return render(request, 'rankingCommiters.html', context)
