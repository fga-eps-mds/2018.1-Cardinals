from django.db import models
from pygithub_api_integration.models import Repository


class Weight(models.Model):
    commit = models.IntegerField()
    line_code = models.IntegerField()
    issues_created = models.IntegerField()
    issues_closed = models.IntegerField()
    repository = models.OneToOneField(Repository,
                                      on_delete=models.CASCADE,
                                      primary_key=True)

    def requestWeight(request, repo):

        weight = Weight()

        weight.commit = request.POST['weight_commit']
        weight.line_code = request.POST['weight_line_code']
        weight.issues_created = request.POST['weight_issues_created']
        weight.issues_closed = request.POST['weight_issues_closed']
        weight.repository = repo
        weight.save()

        return weight

    def __str__(self):
        d = {
              'commit_weight': self.commit,
              'line_code_weight': self.line_code,
              'issues_created_weight': self.issues_created,
              'issues_closed_weight': self.issues_closed,
        }
        return str(d)
