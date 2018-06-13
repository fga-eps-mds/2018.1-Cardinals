from django.shortcuts import render
from github import Github
from oauth.credentials import get_credentials
from github import GithubException
from collections import Counter
from datetime import datetime, timedelta


# Create your views here.
def timeIssue(request):
    username, password = get_credentials()
    g = Github(username, password)
    org = g.get_organization("fga-gpp-mds")
    repo = org.get_repo("2018.1-Cardinals")

    issues = repo.get_issues(state="all")
    all_issues = []
    time_open = Counter()

    for issue in issues:
        if issue.pull_request is None:
            created_time = issue.created_at - timedelta(hours=2)
            if issue.state == "closed":
                closed_time = issue.closed_at - timedelta(hours=2)
            else:
                closed_time = datetime.now()
            all_issues.append(issue)

            time_open[(closed_time - created_time).days] += 1

    days = list(time_open.keys())
    days.sort()

    time_open = sorted(time_open.items())

    return render(request, 'timeissue.html', {'repo': days, 'time': time_open})
