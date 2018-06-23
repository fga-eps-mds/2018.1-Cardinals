from collections import Counter
from datetime import datetime

from django.shortcuts import render

from github import Github, PaginatedList, PullRequest

from bokeh.plotting import figure
from bokeh.embed import components

from oauth.credentials import get_credentials
from cardinals.views import divRequest, scriptRequest

username, password = get_credentials()


def analyze_pull_requests(request, organization, repository):

    context = {'script': scriptRequest(),
               'div': divRequest(),
               'repository': repository}

    return render(request, 'bokeh_graph.html', context)
