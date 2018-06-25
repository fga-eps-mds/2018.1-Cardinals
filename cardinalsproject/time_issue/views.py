from django.shortcuts import render
from collections import Counter
from datetime import datetime, timedelta

from bokeh.plotting import figure
from bokeh.embed import components

from api_request.models import RequestIssuesAPI


def get_bar_plot(days, amount):
    plot = figure(plot_width=800, plot_height=500)

    plot.vbar(x=amount, width=0.5, bottom=0, top=days, color="#CAB2D6")

    plot.xaxis.axis_label = 'Tempo que a issue ficou aberta (dias)'
    plot.yaxis.axis_label = 'Quantidade de issues'

    plot.title.text = 'Período em que as issues ficam abertas'
    plot.title.align = 'center'
    plot.title.text_font_size = '20pt'

    return plot


def analyze_issue_graph(request, organization, repository):
    issuesRequest = RequestIssuesAPI(organization, repository)
    time_open = Counter()

    for issue in issuesRequest.issues:
        time_open[issue.duration] += 1

    amount = list( time_open.keys() )
    days = list( time_open.values() )
    days.sort()

    plot = get_bar_plot( days, amount )
    script, div = components(plot)

    context = {'script': script,
               'div': div,
               'repository': organization + '/' + repository}

    return render(request, 'time_issue.html', context)
