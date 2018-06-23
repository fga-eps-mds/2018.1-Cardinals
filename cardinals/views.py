from django.shortcuts import render, redirect, reverse
from django.views import View
from django.shortcuts import render
from github import Github, PaginatedList, PullRequest
from oauth.credentials import get_credentials
from collections import Counter, defaultdict
from datetime import timedelta, datetime

from bokeh.plotting import figure
from bokeh.models import DatetimeTickFormatter, ColumnDataSource
from bokeh.embed import components

username, password = get_credentials()
global divCommit, scriptCommit
global divIssue, scriptIssue
global divRequest, scriptRequest

def save_repository_name_in_session(request):
    repository_key = 'repository'
    repository_value = request.POST[repository_key]

    request.session[repository_key] = repository_value


def get_organization_repository_from_session(request):
    return request.session['repository'].split('/')

def get_repository_name_in_session(request):
    return request.session['repository']


class searchRepository(View):
    def post(self, request):
        save_repository_name_in_session(request)
        organization, repository = get_organization_repository_from_session(request)
        kwargs = {'organization': organization,
                  'repository': repository}

        url = reverse('get_repo_info', kwargs=kwargs)
        return redirect(url)

    def get(self, request):
        return render(request, 'index.html')

def get_multi_line_plot(dates, all_amount_by_date, signed_amount_by_date, tamW, tamH):
    plot = figure(plot_width=tamW, plot_height=tamH)

    data = {'xs': [dates, dates],
            'ys': [all_amount_by_date, signed_amount_by_date],
            'labels': ['Individual', 'Pareado'],
            'color': ['red', 'green']}
    source = ColumnDataSource(data)
    plot.multi_line(xs='xs', ys='ys',
                    legend='labels',
                    color='color',
                    source=source)
    plot.xaxis.formatter = DatetimeTickFormatter(hours=["%d %B %Y"],
                                                 days=["%d %B %Y"],
                                                 months=["%d %B %Y"],
                                                 years=["%d %B %Y"],)
    plot.xaxis.axis_label = 'Data dos Commits'
    plot.yaxis.axis_label = 'Quantidade de Commits'
    plot.title.text = 'Commits Pareados X Commits Individuais'
    plot.title.align = 'center'
    plot.title.text_font_size = '13pt'
    return plot

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
    plot = figure(plot_width=500, plot_height=350)

    x_var, y_var = get_opened_time_xy_axis(prs_opened_time)

    x_ticks = [i for i in range(0, max(x_var) + 2, 2)]

    plot.vbar(x=x_var, width=0.5, bottom=0, top=y_var, color="#CAB2D6")

    plot.xaxis.axis_label = 'Tempo aberto (dias)'
    plot.yaxis.axis_label = 'Número de pull requests'
    plot.xaxis.ticker = x_ticks

    plot.title.text = 'Tempo que um pull request fica aberto'
    plot.title.align = 'center'
    plot.title.text_font_size = '13pt'

    return plot

def get_bar_plot(days, amount):
    plot = figure(plot_width=500, plot_height=350)

    plot.vbar(x=amount, width=0.5, bottom=0, top=days, color="#CAB2D6")

    plot.xaxis.axis_label = 'Quantidade de issues'
    plot.yaxis.axis_label = 'Tempo que a issue ficou aberta (dias)'

    plot.title.text = 'Período em que as issues ficam abertas'
    plot.title.align = 'center'
    plot.title.text_font_size = '13pt'

    return plot

def analyze_commits_charts(request, organization, repository, tamW, tamH):
    global divCommit, scriptCommit
    github = Github(username, password)
    repository_url = organization + '/' + repository
    repository = github.get_repo(repository_url)

    all_commit_count = defaultdict(list)
    signed_commit_count = Counter()

    for commit in repository.get_commits():
        real_date = commit.commit.author.date - timedelta(hours=2)
        all_commit_count[real_date.date()].append(commit.commit)
        if (commit.commit.message.count("Co-authored-by:") > 1 or (commit.commit.message.count("Co-authored-by:") == 1)) or (commit.commit.message.count("Signed-off-by:") > 1 or (commit.commit.message.count("Signed-off-by:") == 1 and
            commit.commit.author.email not in commit.commit.message) or ((commit.commit.author.email != commit.commit.committer.email)
            and ("noreply@github.com" not in commit.commit.committer.email))):

            signed_commit_count[real_date.date()] += 1
        else:
            signed_commit_count[real_date.date()] += 0

    commit_count = {k_var: len(var) for k_var, var in all_commit_count.items()}

    dates = list(commit_count.keys())
    dates.sort()

    commit_count = sorted(commit_count.items())
    all_amount_by_date = [x_var[1] for x_var in commit_count]
    signed_commit_count = sorted(signed_commit_count.items())
    signed_amount_by_date = [x_var[1] for x_var in signed_commit_count]

    plot = get_multi_line_plot(dates, all_amount_by_date, signed_amount_by_date, tamW, tamH)
    script, div = components(plot)
    
    divCommit = div
    scriptCommit = script

def analyze_issue_graph(request, organization, repository):
    global divIssue, scriptIssue

    github = Github(username, password)
    repository_url = organization + '/' + repository
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
    amount = [x_var[1] for x_var in time_open]

    plot = get_bar_plot(days, amount)
    script, div = components(plot)

    divIssue = div
    scriptIssue = script

def analyze_pull_requests(request, organization, repository):
    global divRequest, scriptRequest

    github = Github(username, password)
    repository_url = organization + '/' + repository
    repository = github.get_repo(repository_url)

    pull_requests = repository.get_pulls(state='all')

    prs_opened_time = get_pull_requests_opened_time(pull_requests)
    plot = get_vbar_plot(prs_opened_time)
    script, div = components(plot)

    divRequest = div
    scriptRequest = script

def scriptCommit():
    return scriptCommit

def divCommit():
    return divCommit

def scriptIssue():
    return scriptIssue

def divIssue():
    return divIssue

def scriptRequest():
    return scriptRequest

def divRequest():
    return divRequest