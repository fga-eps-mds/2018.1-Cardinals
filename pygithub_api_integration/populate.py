from github import Github
from oauth.credentials import get_credentials
from operator import itemgetter
from pygithub_api_integration.models import *

username, password = get_credentials()

g = Github(username, password)
org = g.get_organization('fga-gpp-mds')
repo = org.get_repo('2018.1-Cardinals')



stats_contributors = repo.get_stats_contributors()

for sc in stats_contributors:
    contributors = Contributor()
    contributors.id = sc.author.id
    contributors.username =  sc.author.name
    contributors.commits = sc.total
    contributors.line_code = getLineCode(sc)
    contributors.issues_created = getIssuesCreatedFor(sc.author.id)
    contributors.issues_closed = 0
    contributors.save()


def getLineCode(contributors):

    line_code = 0
    weeks = contributors.weeks

    for week in weeks:
        line_code += week.a - week.d

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


                        

   