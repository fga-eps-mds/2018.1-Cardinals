from django.shortcuts import render
from github import Github
from github import GithubException as GE
from oauth.credentials import get_credentials 
from collections import *
from datetime import datetime, timedelta

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

username, password = get_credentials()
dates=[]
all_amount_by_date=[]
signed_amount_by_date=[]



def commits_charts(commits_charts):
    
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


    return (dates, all_amount_by_date, signed_amount_by_date)
    

def get_multi_line_plot(commits_charts):
    plot = figure(plot_width=800, plot_height=500)

    dates = commits_charts(commits_charts)
    all_amount_by_date = commits_charts(commits_charts)
    signed_amount_by_date = commits_charts(commits_charts)
    
    plot.multi_line(xs=[dates,dates], ys= [all_amount_by_date,signed_amount_by_date],
             color=['red','green'])
    
    plot.xaxis.axis_label = 'Data do Commit'
    plot.yaxis.axis_label = 'Commits'
    """ plot.xaxis.ticker = x_ticks """

    plot.title.text = 'Commits Pareados X Commits Individuais'
    plot.title.align = 'center'
    plot.title.text_font_size = '20pt'

    return plot


def analyze_commits_charts(request, organization, repository):

    repository_url = organization + '/' + repository
    github = Github(username, password)
    repository = github.get_repo(repository_url)
    plot = get_multi_line_plot(commits_charts)
    script, div = components(plot)

    context = {'script': script,
               'div': div,
               'repository': repository_url}

    return render(request, 'bokeh_graph.html', context)

