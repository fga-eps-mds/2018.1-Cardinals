from django.shortcuts import render, redirect, reverse
from django.views import View
from django.shortcuts import render
from github import Github
from oauth.credentials import get_credentials
from collections import Counter, defaultdict
from datetime import timedelta

from bokeh.plotting import figure
from bokeh.models import DatetimeTickFormatter, ColumnDataSource
from bokeh.embed import components

username, password = get_credentials()

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


def analyze_commits_charts(request, organization, repository, tamW, tamH):

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

    context = {'script': script,
               'div': div,
               'repository': repository_url}

    return [div, script]
