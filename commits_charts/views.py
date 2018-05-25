from django.shortcuts import render
from github import Github
from github import GithubException as GE
from oauth.credentials import get_credentials 
from collections import *
from datetime import datetime, timedelta

def commits_charts(request):
    username, password = get_credentials()
    g = Github(username, password)
    user = g.get_user()
    org = g.get_organization("fga-gpp-mds")
    repos = user.get_repos()
    repo = org.get_repo("2018.1-Cardinals")


    all_commit_count = defaultdict(list)
    signed_commit_count = Counter()

    for commit in repo.get_commits():
        real_date = commit.commit.author.date - timedelta(hours=2)
        all_commit_count[real_date.date()].append(commit.commit)
#     for saved_commit in all_commit_count[real_date.date()]:
#         if "Merge" in saved_commit.message or "Merging" in saved_commit.message:
#             all_commit_count[real_date.date()].remove(saved_commit)
        if (commit.commit.message.count("Co-authored-by:") > 1 or (commit.commit.message.count("Co-authored-by:") == 1)) or (commit.commit.message.count("Signed-off-by:") > 1 or (commit.commit.message.count("Signed-off-by:") == 1 and
            commit.commit.author.email not in commit.commit.message) or ((commit.commit.author.email != commit.commit.committer.email) 
            and ("noreply@github.com" not in commit.commit.committer.email))):

            signed_commit_count [real_date.date()] += 1
        else:
            signed_commit_count [real_date.date()] += 0

    commit_count = {k: len(v) for k, v in all_commit_count.items()}
        
    dates = list(commit_count.keys())
    dates.sort()

    commit_count = sorted(commit_count.items())
    all_amount_by_date = [x[1] for x in commit_count]
    signed_commit_count = sorted(signed_commit_count.items())
    signed_amount_by_date = [x[1] for x in signed_commit_count]


    return render(request, 'commits_charts.html' 
                         , {'dates': dates
                         ,  'all_commits': all_amount_by_date
                         ,  'signed_commits': signed_amount_by_date})
