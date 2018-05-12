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
        weight_issues_created = 1
        weight_issues_closed = 1

        weight_commit = request.GET['weight_commit']
        weight_issues_created = request.GET['weight_issues_created']
        weight_issues_closed = request.GET['weight_issues_closed']

        for rc in contributors:
            commiters.append({"name": contributors["name"],
                              "score": contributors["commits"] * weight_commit +
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
                             "issues_created": getIssuesCreatedFor(sc.author.id),
                             "issues_closed": getIssuesClosedFor(sc.author.id)
                             })

    return contributors


def getIssuesCreatedFor(contributor_id):

    issues_all = repo.get_issues(state="all")
    num_issues_created = 0
    index_issue = issues_all[0].number - 1

    while index_issue >= 0:
        if issues_all[index_issue].user.id == contributor_id:
            num_issues_created += 1

        index_issue -= 1

    return num_issues_created


def getIssuesClosedFor(contributor_id):

    issues_all = repo.get_issues(state="all")
    num_issues_closed = 0
    index_issue = issues_all[0].number - 1

    while index_issue >= 0:
        if issues_all[index_issue].state == "closed":
            if issues_all[index_issue].closed_by.id == contributor_id:
                num_issues_closed += 1

        index_issue -= 1

    return num_issues_closed
