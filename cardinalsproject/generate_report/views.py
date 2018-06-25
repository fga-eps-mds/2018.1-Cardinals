import pdfcrowd

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

from django.http import HttpResponse
from api_request.models import *

# from pygithub_api_integration.models import Repository
# from pygithub_api_integration.models import Contributor
from ranking_commiters.models import Weight


def create_pdf_paragraph(vector, text, size):

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size=%d>%s</font>' % (size, text)

    vector.append(Paragraph(ptext, styles["Normal"]))


def create_pdf_space(vector, size):
    vector.append(Spacer(1, size))


def create_pdf_img(vector, img_obj, image):

    img_obj = Image(image, 7 * inch, 3.5 * inch)
    vector.append(img_obj)


def config_convert_img():

    user_api_pdfcrowd = 'mateusas3s'
    key_api_pdfcrowd = '7aa4ecdff52221464868419a3f842b00'

    img_config = pdfcrowd.HtmlToImageClient(user_api_pdfcrowd,
                                            key_api_pdfcrowd)

    # configure the conversion
    img_config.setOutputFormat('jpg')

    return img_config


def convert_html2image(img_obj, path_html, path_jpg):

    # run the conversion and write the result to a file
    img_obj.convertFileToFile(path_html, path_jpg)

    return path_jpg


def pdf_view(request, organization, repository):

    name = organization + '/' + repository

    repo = RepositoryAPI(organization, repository)
    weight = Weight.create_from_request(request)
    repo.update_score(weight)

    ranking_commiters = repo.contributors

    report_name = 'attachment; filename=Relatorio_' + repo.full_name + '.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = report_name

    pdf = SimpleDocTemplate(response, pagesize=A4)

    Story = []

    create_pdf_paragraph(Story, repo.full_name, 16)
    create_pdf_space(Story, 12)

    create_pdf_paragraph(Story, "Contribuidores", 12)
    create_pdf_space(Story, 10)

    for c in ranking_commiters:
        contrib = c.name + ' / ' + c.login + ' | ' + str(c.score)
        create_pdf_paragraph(Story, contrib, 10)

    img_obj = config_convert_img()

    chart_commit = convert_html2image(img_obj,
                                      'static/images/charts/chart_commit.html',
                                      'static/images/charts/chart_commit.jpg')
    create_pdf_img(Story, img_obj, chart_commit)

    chart_pr = convert_html2image(img_obj,
                                  'static/images/charts/chart_pr.html',
                                  'static/images/charts/chart_pr.jpg')
    create_pdf_img(Story, img_obj, chart_pr)

    chart_issue = convert_html2image(img_obj,
                                     'static/images/charts/chart_issue.html',
                                     'static/images/charts/chart_issue.jpg')
    create_pdf_img(Story, img_obj, chart_issue)

    pdf.build(Story)

    return response
