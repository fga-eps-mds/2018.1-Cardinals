from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse
from pygithub_api_integration.models import Repository
from pygithub_api_integration.models import Contributor


def pdfView(request, repo_id):

    repo = Repository.objects.get(id=repo_id)

    commiters = Contributor.objects.filter(repository=repo_id)

    response = HttpResponse(content_type='application/pdf')
    report_name = 'attachment; filename=Relatorio_' + repo.name + '.pdf'
    response['Content-Disposition'] = report_name

    pdf = canvas.Canvas(response, pagesize=A4)

    pdf.setFont('Times-Bold', 32)
    pdf.drawString(50, 760, repo.name)

    pdf.drawImage('static/images/charts/chart_pr.png', 50, 500,
                  width=300, height=200)

    pdf.showPage()
    pdf.save()
    return response
