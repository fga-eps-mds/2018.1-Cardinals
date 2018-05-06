from django.shortcuts import render
from github import Github
from oauth.credentials import get_credentials

username, password = get_credentials()

g = Github(username, password)
org = g.get_organization('fga-gpp-mds')
repo = org.get_repo('2018.1-Cardinals')


def getRankingCommiters(request):

    rankingCommiters = scoreContributor()

    return render(request, 'rankingCommiters.html',
                  {"rankingCommiters": rankingCommiters})


def getStatsContributors():

    contributors = {}

    stats_contributors = repo.get_stats_contributors()

    for sc in stats_contributors:
        contributors[sc.author.id] = {"name": sc.author.name,
                                      "commits": sc.total}

    return contributors


def getIssuesCreatedFor(contributor):

    issues_created = repo.get_issues(creator=contributor)
    num_issues_created = 0

    for i in issues_created:
        num_issues_created += 1

    return num_issues_created


def getIssuesClosedFor(contributor):

    issues_closed = repo.get_issues(state="closed")

    for i in issues_closed:
        if i.closed_by == contributor:
            issues_closed_for_contributor = issues_closed

    return issues_closed_for_contributor


def scoreContributor():

    contributors_ranked = []

    stats_contributors = getStatsContributors()

    for i, sc in stats_contributors:
        contributors_ranked[i] = {"nome": sc.author.name,
                                  "commits": sc.total,
                                  "issues_created": getIssuesCreatedFor(sc.author),
                                  "issue_closed": getIssuesClosedFor(sc.author)
                                  }
    return contributors_ranked
