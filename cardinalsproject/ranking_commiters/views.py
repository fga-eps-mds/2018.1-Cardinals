from django.shortcuts import render
from operator import attrgetter

from api_request.models import *

from ranking_commiters.models import Weight


def ranking_commiters(request, organization, repository):

    repository = RepositoryAPI(organization, repository)
    weight = Weight()

    if request.method == 'POST':
        weight = Weight(request)

    weight.save_in_session(request)
    repository.update_score(weight)
    commiters = repository.contributors

    ranking_commiters = sorted(commiters,
                               key=attrgetter('score'),
                               reverse=True)

    context = {"repo_id": 0, "ranking_commiters": ranking_commiters}

    return render(request, 'rankingCommiters.html', context)
