from django.shortcuts import render
from github import Github
from oauth.credentials import get_credentials
from operator import itemgetter

username, password = get_credentials()

g = Github(username, password)
org = g.get_organization('fga-gpp-mds')
repo = org.get_repo('2018.1-Cardinals')


def getRankingCommiters(request):
    return render(request, 'rankCommiters.html')


def getRankingCommitersResult(request):

    if request.method == 'GET':

        commiters = []
        contributors = getStatsContributors()

        weight_commit = 1
        weight_line_code = 1
        weight_issues_created = 1
        weight_issues_closed = 1

        weight_commit = request.GET['weight_commit']
        weight_line_code = request.GET['weight_line_code']
        weight_issues_created = request.GET['weight_issues_created']
        weight_issues_closed = request.GET['weight_issues_closed']

        for rc in contributors:
            commiters.append({"name": contributors["name"],
                              "score": contributors["commits"] * weight_commit +
                              contributors["line_code"] * weight_line_code +
                              contributors["issues_created"] * weight_issues_created +
                              contributors["issues_closed"] * weight_issues_closed})

        ranking_commiters = sorted(commiters, key=itemgetter("score"), reverse=True)

        return render(request, 'rankingCommiters.html',
                      {"ranking_commiters": ranking_commiters})

    elif request.method == 'POST':
        commiters = []
        contributors = getStatsContributors()

        for rc in contributors:
            commiters.append({"name": contributors["name"],
                              "score": contributors["commits"] +
                              contributors["line_code"] +
                              contributors["issues_created"] +
                              contributors["issues_closed"]})

        ranking_commiters = sorted(commiters, key=itemgetter("score"), reverse=True)

        return render(request, 'rankingCommiters.html',
                      {"ranking_commiters": ranking_commiters})


def getStatsContributors():

    contributors = []

    stats_contributors = repo.get_stats_contributors()

    for sc in stats_contributors:
        contributors.append({"name": sc.author.name,
                             "commits": sc.total,
                             "line_code": getLineCode(sc),
                             "issues_created": getIssuesCreatedFor(sc.author.id),
                             "issues_closed": getIssuesClosedFor(sc.author.id)
                             })

    return contributors


def getLineCode(contributors):

    line_code = 0
    weeks = contributors.weeks

    for week in weeks:
        line_code += weeks.a - weeks.d

    return line_code


def getIssuesCreatedFor(contributor_id):

    issues_all = repo.get_issues(state="all")
    num_issues_created = 0

    for issue in issues_all:
        if issue.user.id == contributor_id:
            num_issues_created += 1

    return num_issues_created


def getIssuesClosedFor(contributor_id):

    issues_all = repo.get_issues(state="all")
    num_issues_closed = 0

    for issue in issues_all:
        if issue.state == "closed":
            if issue.closed_by.id == contributor_id:
                num_issues_closed += 1

    return num_issues_closed
