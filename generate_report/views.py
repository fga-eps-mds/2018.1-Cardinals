from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse
from pygithub_api_integration.models import Repository
from pygithub_api_integration.models import Contributor
from ranking_commiters.models import Weight

MARGIN_LEFT = 50
SPACE_VERT = 20


def pdfView(request, repo_id):

    repo = Repository.objects.get(id=repo_id)
    commiters = Contributor.objects.filter(repository=repo_id)
    weight = Weight.objects.get(repository=repo_id)

    Contributor.getScore(commiters, weight)

    response = HttpResponse(content_type='application/pdf')
    report_name = 'attachment; filename=Relatorio_' + repo.name + '.pdf'
    response['Content-Disposition'] = report_name

    pdf = canvas.Canvas(response, pagesize=A4)

    pdf.setFont('Times-Bold', 28)
    pdf.drawString(MARGIN_LEFT, SPACE_VERT * 40, repo.name)

    line_down = 0

    for c in commiters:
        pdf.setFont('Times-Bold', 10)
        pdf.drawString(MARGIN_LEFT + 10, SPACE_VERT * (30 - line_down),
                       c.name + '/' + c.login + ' | ' + str(c.score))

        line_down -= 0.8

    pdf.drawImage('static/images/charts/chart_commit.png',
                  MARGIN_LEFT + 10, SPACE_VERT + 300,
                  width=300, height=200)

    pdf.drawImage('static/images/charts/chart_pr.png',
                  MARGIN_LEFT + 10, SPACE_VERT,
                  width=300, height=200)

    pdf.showPage()
    pdf.save()
    return response
