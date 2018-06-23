from django.shortcuts import render
from github import Github
from github import GithubException as GE
from oauth.credentials import get_credentials
from collections import Counter, defaultdict
from datetime import datetime, timedelta

from bokeh.plotting import figure, output_file, show
from bokeh.models import DatetimeTickFormatter, ColumnDataSource
from bokeh.embed import components
from cardinals.views import get_multi_line_plot, divCommit, scriptCommit

username, password = get_credentials()

def analyze_commits_charts(request, organization, repository):

    context = {'script': scriptCommit(),
               'div': divCommit(),
               'repository': repository}

    return render(request, 'commits_charts.html', context)