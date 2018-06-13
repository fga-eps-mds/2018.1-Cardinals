from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse
from pygithub_api_integration.models import Repository
from pygithub_api_integration.models import Contributor
from generate_report.models import Report


def pdfView(request, repo_id):

    repo = Repository.objects.get(id=repo_id)
    report_id = Report.savePdf(repo)
    report = Report.objects.get(id=report_id)
    # commiters = Contributor.objects.filter(repository=repo_id)

    response = HttpResponse(content_type='application/pdf')
    report_name = 'attachment; filename=Relatorio_' + repo.name + '.pdf'
    response['Content-Disposition'] = report_name

    pdf = canvas.Canvas(response, pagesize=A4)

    pdf.drawString(100, 100, "Hello world.")

    pdf.showPage()
    pdf.save()
    return response
