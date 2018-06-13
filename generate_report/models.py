from django.db import models
from pygithub_api_integration.models import Repository


class Report(models.Model):
    id = models.AutoField(primary_key=True)
    repo_name = models.CharField(max_length=255, null=False)
    chart_pr = models.ImageField()
    chart_commit = models.ImageField()
    chart_issue = models.ImageField()
    repository = models.ForeignKey('Repository',
                                   on_delete=models.CASCADE)


class Commiter(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    login = models.CharField(max_length=255)
    score = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    report = models.ManyToManyField(Report)


class Doc(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.BooleanField(max_length=255)
    report = models.ManyToManyField(Report)
