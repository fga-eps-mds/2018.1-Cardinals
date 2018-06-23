from django.shortcuts import render
from github import Github
from oauth.credentials import get_credentials
from collections import Counter
from datetime import datetime, timedelta

from bokeh.plotting import figure
from bokeh.embed import components
from cardinals.views import scriptIssue, divIssue

username, password = get_credentials()

def analyze_issue_graph(request, organization, repository):

    context = {'script': scriptIssue(),
               'div': divIssue(),
               'repository': repository}

    return render(request, 'time_issue.html', context)
