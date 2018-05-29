from django.db import models


class Weight(models.Model):
    commit = models.IntegerField()
    line_code = models.IntegerField()
    issues_created = models.IntegerField()
    issues_closed = models.IntegerField()
