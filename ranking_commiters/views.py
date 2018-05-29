from django.shortcuts import render
from operator import attrgetter
from pygithub_api_integration.models import Contributor
from ranking_commiters.models import Weight


def getResult(request, repo_id):

    commiters = Contributor.objects.filter(repository=repo_id)

    if request.method == 'GET':

        commiters = Contributor.getScore(commiters)

    elif request.method == 'POST':

        weight = Weight()

        weight.commit = request.POST['weight_commit']
        weight.line_code = request.POST['weight_line_code']
        weight.issues_created = request.POST['weight_issues_created']
        weight.issues_closed = request.POST['weight_issues_closed']

        weight.save()

        commiters = Contributor.getScore(commiters, weight=weight)

    ranking_commiters = sorted(commiters,
                               key=attrgetter('score'),
                               reverse=True)

    return render(request, 'rankingCommiters.html',
                  {"ranking_commiters": ranking_commiters})
