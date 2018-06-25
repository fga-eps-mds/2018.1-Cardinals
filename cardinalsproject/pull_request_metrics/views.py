from collections import Counter
from datetime import datetime

from django.shortcuts import render

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

from api_request.models import RequestPullRequest


def get_vbar_plot(x_var, y_var):
    plot = figure(plot_width=800, plot_height=500)

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

    requestPR = RequestPullRequest(organization, repository)

    time_open = Counter()

    for pr in requestPR.pulls:
        time_open[pr.duration] += 1

    days = list( time_open.keys() )
    amount = list( time_open.values() )
    days.sort()

    plot = get_vbar_plot(days,amount)
    script, div = components(plot)

    output_file("static/images/charts/chart_pr.html")
    show(plot)

    context = {'script': script,
               'div': div,
               'repository': organization + '/' + repository }

    return render(request, 'bokeh_graph.html', context)
