from django.shortcuts import render
from operator import attrgetter
from pygithub_api_integration.models import Contributor


def getRankingCommitersResult(request):
    if request.method == 'GET':
        commiters = Contributor.getStatsContributors()

    elif request.method == 'POST':

        weight = {}

        weight["commit"] = request.POST['weight_commit']
        weight["line_code"] = request.POST['weight_line_code']
        weight["issues_created"] = request.POST['weight_issues_created']
        weight["issues_closed"] = request.POST['weight_issues_closed']

        commiters = Contributor.getStatsContributors(weight)

    ranking_commiters = sorted(commiters,
                               key=attrgetter('score'),
                               reverse=True)

    return render(request, 'rankingCommiters.html',
                  {"ranking_commiters": ranking_commiters})

    # if request.method == 'GET':

    #     commiters = []
    #     contributors = getStatsContributors()

    #     weight_commit = 1
    #     weight_line_code = 1
    #     weight_issues_created = 1
    #     weight_issues_closed = 1

    #     weight_commit = request.GET['weight_commit']
    #     weight_line_code = request.GET['weight_line_code']
    #     weight_issues_created = request.GET['weight_issues_created']
    #     weight_issues_closed = request.GET['weight_issues_closed']

    #     for rc in contributors:
    #         commiters.append({"name": contributors["name"],
    #                           "score": contributors["commits"] *
    #                           weight_commit +
    #                           contributors["line_code"] *
    #                           weight_line_code +
    #                           contributors["issues_created"] *
    #                           weight_issues_created +
    #                           contributors["issues_closed"] *
    #                           weight_issues_closed})

    #     ranking_commiters = sorted(commiters,
    #                                key=itemgetter("score"),
    #                                reverse=True)

    #     return render(request, 'rankingCommiters.html',
    #                   {"ranking_commiters": ranking_commiters})


# def getStatsContributors():

#     contributors = []

#     stats_contributors = repo.get_stats_contributors()

#     for s in stats_contributors:
#         contributors.append({"name": s.author.name,
#                              "commits": s.total,
#                              "line_code": getLineCode(s),
#                              "issues_created": getIssuesCreated(s.author.id),
#                              "issues_closed": getIssuesClosed(s.author.id)
#                              })

#     return contributors


# def getLineCode(contributors):

#     line_code = 0
#     weeks = contributors.weeks

#     for week in weeks:
#         line_code += weeks.a - weeks.d

#     return line_code


# def getIssuesCreated(contributor_id):

#     issues_all = repo.get_issues(state="all")
#     num_issues_created = 0

#     for issue in issues_all:
#         if issue.user.id == contributor_id:
#             num_issues_created += 1

#     return num_issues_created


# def getIssuesClosed(contributor_id):

#     issues_all = repo.get_issues(state="all")
#     num_issues_closed = 0

#     for issue in issues_all:
#         if issue.state == "closed":
#             if issue.closed_by.id == contributor_id:
#                 num_issues_closed += 1

#     return num_issues_closed
