from django.shortcuts import render

from api_request.models import CommitsChartAPI

from bokeh.plotting import figure
from bokeh.models import DatetimeTickFormatter, ColumnDataSource
from bokeh.embed import components


def get_multi_line_plot(dates, all_amount_by_date, signed_amount_by_date):
    plot = figure(plot_width=800, plot_height=500)

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
    plot.title.text_font_size = '20pt'
    return plot


def analyze_commits_charts(request, organization, repository):

    full_name = organization + '/' + repository
    chartData = CommitsChartAPI(organization, repository)

    plot = get_multi_line_plot(chartData.dates, chartData.commits, chartData.paired)
    script, div = components(plot)

    context = {'script': script,
               'div': div,
               'repository': full_name}

    return render(request, 'commits_charts.html', context)
