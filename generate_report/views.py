from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse
from pygithub_api_integration.models import Repository
from pygithub_api_integration.models import Contributor
from pygithub_api_integration.models import Report


def pdfView(request, repo_id):

    repo = Repository.objects.get(id=repo_id)
    report_id = Report.savePdf(repo)
    report = Report.objects.get(id=report_id)
    # commiters = Contributor.objects.filter(repository=repo_id)

    response = HttpResponse(content_type='application/pdf')
    report_name = 'attachment; filename=Relatorio_' + report.repo_name + '.pdf'
    response['Content-Disposition'] = report_name

    pdf = canvas.Canvas(response, pagesize=A4)

    pdf.setFont('Times-Bold', 32)
    pdf.drawString(50, 750, report.repo_name)

    canvas.drawImage(report.chart_pr, 50, 700)

    pdf.showPage()
    pdf.save()
    return response
