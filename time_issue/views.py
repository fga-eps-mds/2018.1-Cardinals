from django.shortcuts import render
from github import Github
from oauth.credentials import get_credentials
from github import GithubException
from collections import Counter
from datetime import datetime, timedelta

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components




username, password = get_credentials()

# Create your views here.
def timeIssue(request):
    username, password = get_credentials()
    g = Github(username, password)
    user = g.get_user()
    org = g.get_organization("fga-gpp-mds")
    repos = user.get_repos()
    repo = org.get_repo("2018.1-Cardinals")
   
    issues = repo.get_issues(state="all")
    all_issues = []
    time_open = Counter()


    for issue in issues:
        if issue.pull_request == None:
            created_time = issue.created_at - timedelta(hours=2)
            if issue.state == "closed":
                closed_time = issue.closed_at - timedelta(hours=2)
            else:
                closed_time = datetime.now()
            all_issues.append(issue)
            
            time_open[(closed_time - created_time).days] += 1

    days = list(time_open.keys())
    days.sort()
    print(days)

    time_open = sorted(time_open.items())
    amount = [x[1] for x in time_open]
    print(amount)

    mean = sum(amount)/len(amount)  
    return render({'repo' : days, 'time' : time_open})

def get_multi_line_plot(timeIssue):
    plot = figure(plot_width=800, plot_height=500)

    plot.multi_line(xs=[[1, 2, 3], [2, 3, 4]], ys=[[6, 7, 2], [4, 5, 7]],
             color=['red','green'])
    
    plot.xaxis.axis_label = 'Data do Commit'
    plot.yaxis.axis_label = 'Commits'
    """ plot.xaxis.ticker = x_ticks """

    plot.title.text = 'Commits Pareados X Commits Individuais'
    plot.title.align = 'center'
    plot.title.text_font_size = '20pt'

    return plot
def analyze_issue_graph(request, organization, repository):

    repository_url = organization + '/' + repository
    github = Github(username, password)
    repository = github.get_repo(repository_url)
    plot = get_multi_line_plot(timeIssue)
    script, div = components(plot)

    context = {'script': script,
               'div': div,
               'repository': repository_url}

    return render(request, 'bokeh_graph.html', context)