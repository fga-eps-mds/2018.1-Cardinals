from django.db import models
from pygithub_api_integration.models import Repository


class Report(models.Model):
    id = models.AutoField(primary_key=True)
    repo_name = models.CharField(max_length=255, null=False)
    chart_pr = models.ImageField(null=True)
    chart_commit = models.ImageField(null=True)
    chart_issue = models.ImageField(null=True)
    repository = models.ForeignKey(Repository,
                                   on_delete=models.CASCADE)

    def savePdf(repo):
        report = Report()
        report.repo_name = repo.name
        report.chart_pr = '../static/images/charts/chart_pr.png'
        report.chart_commit = '../static/images/charts/chart_commit.png'
        report.chart_issue = '../static/images/charts/chart_issue.png'
        report.repository = repo
        report.save()

        return report.id


# class Commiter(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     name = models.CharField(max_length=255, null=True)
#     login = models.CharField(max_length=255, null=True)
#     score = models.DecimalField(max_digits=9, decimal_places=2, null=True)
#     report = models.ManyToManyField(Report)


# class Doc(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255, null=True)
#     status = models.BooleanField(max_length=255, null=True)
#     report = models.ManyToManyField(Report)
