from django.shortcuts import render
from github import Github
from oauth.credentials import get_credentials
from github import GithubException
from collections import Counter
from datetime import datetime, timedelta

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

username, password = get_credentials()


def get_bar_plot(days, amount):
    plot = figure(plot_width=800, plot_height=500)

    plot.vbar(x=amount, width=0.5, bottom=0, top=days, color="#CAB2D6")

    plot.xaxis.axis_label = 'Quantidade de issues'
    plot.yaxis.axis_label = 'Tempo que a issue ficou aberta (dias)'
    """ plot.xaxis.ticker = x_ticks """

    plot.title.text = 'Período em que as issues ficam abertas'
    plot.title.align = 'center'
    plot.title.text_font_size = '20pt'

    return plot


def analyze_issue_graph(request, organization, repository):

    repository_url = organization + '/' + repository
    github = Github(username, password)
    repository = github.get_repo(repository_url)

    issues = repository.get_issues(state="all")
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
    amount = [x[1] for x in time_open]

    # mean = sum(amount) / len(amount)

    plot = get_bar_plot(days, amount)
    script, div = components(plot)

    context = {'script': script,
               'div': div,
               'repository': repository_url}

    return render(request, 'time_issue.html', context)
