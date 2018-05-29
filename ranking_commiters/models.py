from django.db import models
from pygithub_api_integration.models import Repository


class Weight(models.Model):
    commit = models.IntegerField()
    line_code = models.IntegerField()
    issues_created = models.IntegerField()
    issues_closed = models.IntegerField()
    repository = models.ForeignKey(Repository,
                                   on_delete=models.CASCADE)
