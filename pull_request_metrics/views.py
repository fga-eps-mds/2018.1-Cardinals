from collections import Counter
from datetime import datetime

from django.shortcuts import render

from github import Github, PaginatedList, PullRequest

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

from oauth.credentials import get_credentials


username, password = get_credentials()


def get_pull_request_opened_time(pull_request):
    assert isinstance(pull_request, PullRequest.PullRequest)

    time_open = pull_request.created_at
    time_close = pull_request.closed_at

    if time_close is None:
        time_close = datetime.now()

    opened_time = (time_close - time_open)
    return opened_time


def get_pull_requests_opened_time(pull_requests):
    assert isinstance(pull_requests, PaginatedList.PaginatedList)

    opened_times = [get_pull_request_opened_time(pr) for pr in pull_requests]
    return opened_times


def get_opened_time_xy_axis(prs_opened_time):
    counter = Counter(opened_time.days for opened_time in prs_opened_time)

    x = list(counter.keys())
    y = list(counter.values())
    return (x, y)


def get_vbar_plot(prs_opened_time):
    plot = figure(plot_width=800, plot_height=500)

    x_var, y_var = get_opened_time_xy_axis(prs_opened_time)

    x_ticks = [i for i in range(0, max(x_var) + 2, 2)]

    plot.vbar(x=x_var, width=0.5, bottom=0, top=y_var, color="#CAB2D6")

    plot.xaxis.axis_label = 'Tempo aberto (dias)'
    plot.yaxis.axis_label = 'Número de pull requests'
    plot.xaxis.ticker = x_ticks

    plot.title.text = 'Tempo que um pull request fica aberto'
    plot.title.align = 'center'
    plot.title.text_font_size = '20pt'

    return plot


def analyze_pull_requests(request, organization, repository):

    github = Github(username, password)
    repository_url = organization + '/' + repository
    repository = github.get_repo(repository_url)

    pull_requests = repository.get_pulls(state='all')

    output_file("static/images/charts/chart_pr.html")

    prs_opened_time = get_pull_requests_opened_time(pull_requests)
    plot = get_vbar_plot(prs_opened_time)

    script, div = components(plot)

    show(plot)

    context = {'script': script,
               'div': div,
               'repository': repository_url}

    return render(request, 'bokeh_graph.html', context)
