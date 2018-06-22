from django.shortcuts import render
from operator import attrgetter
from pygithub_api_integration.models import Contributor
from pygithub_api_integration.models import Repository
from pygithub_api_integration.models import Issue
from pygithub_api_integration.views import populate_db_if_data_is_old
from ranking_commiters.models import Weight
from cardinals.views import get_repository_name_in_session

def ranking_commiters(request, organization, repository):

    name = organization + '/' + repository
    repo = populate_db_if_data_is_old(name)
    repo_id = repo.id

    if request.method == 'GET':

        repo_request = Repository.requestRepo(repo.full_name)

        issue_request = Issue.requestIssues(repo_request)
        Issue.saveIssues(issue_request, repo)

        commiters = Contributor.objects.filter(repository=repo_id)

        Contributor.setLineCodeContrib(commiters)
        Contributor.setIssuesCreatedFor(commiters, repo_id)
        Contributor.setIssuesClosedFor(commiters, repo_id)

        commiters = Contributor.getScore(commiters)

    elif request.method == 'POST':

        commiters = Contributor.objects.filter(repository=repo_id)

        weight = Weight.requestWeight(request)

        commiters = Contributor.getScore(commiters, weight=weight)

    ranking_commiters = sorted(commiters,
                               key=attrgetter('score'),
                               reverse=True)

    context = {"repo_id": repo_id, "ranking_commiters": ranking_commiters}

    return render(request, 'rankingCommiters.html', context)

