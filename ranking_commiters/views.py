from django.shortcuts import render
from github import Github
from oauth.credentials import get_credentials

username, password = get_credentials()

g = Github(username, password)
org = g.get_organization('fga-gpp-mds')
repo = org.get_repo('2018.1-Cardinals')


def getRankingCommiters(request):

    rankingCommiters = getStatsContributors()

    return render(request, 'rankingCommiters.html',
                  {"rankingCommiters": rankingCommiters})


def getStatsContributors():

    contributors = []

    stats_contributors = repo.get_stats_contributors()

    for sc in stats_contributors:
        contributors.append({"id": sc.author.id,
                             "name": sc.author.name,
                             "commits": sc.total,
                             "issues_created": getIssuesCreatedFor(sc.author.id)
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
