import time

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

from django.http import HttpResponse

from pygithub_api_integration.models import Repository
from pygithub_api_integration.models import Contributor
from ranking_commiters.models import Weight

MARGIN_LEFT = 50
SPACE_VERT = 20
LINE = 213
CENTER_PAG = 300


def pdfView(request, repo_id):

    repo = Repository.objects.get(id=repo_id)
    commiters = Contributor.objects.filter(repository=repo_id)
    weight = Weight.objects.get(repository=repo_id)

    ranking_commiters = Contributor.getScore(commiters, weight)

    response = HttpResponse(content_type='application/pdf')
    report_name = 'attachment; filename=Relatorio_' + repo.full_name + '.pdf'
    response['Content-Disposition'] = report_name

    pdf = SimpleDocTemplate(response, pagesize=A4)

    Story = []

    # nome do repositório
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size=16>%s</font>' % repo.full_name

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    # contribuidores
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size=12>%s</font>' % "Contribuidores"

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 4))

    for c in ranking_commiters:
        contrib = c.name + ' / ' + c.login + ' | ' + str(c.score)
        ptext = '<font size=10>%s</font>' % contrib
        Story.append(Paragraph(ptext, styles["Normal"]))

    pdf.build(Story)

    return response
