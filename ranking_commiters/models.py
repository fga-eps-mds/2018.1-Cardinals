from django.db import models


class Weight(models.Model):
    commit = models.IntegerField()
    line_code = models.IntegerField()
    issues_created = models.IntegerField()
    issues_closed = models.IntegerField()

    def requestWeight(request):

        weight = Weight()

        weight.commit = request.POST['weight_commit']
        weight.line_code = request.POST['weight_line_code']
        weight.issues_created = request.POST['weight_issues_created']
        weight.issues_closed = request.POST['weight_issues_closed']

        return weight

    def __str__(self):
        d = {
              'commit_weight': self.commit,
              'line_code_weight': self.line_code,
              'issues_created_weight': self.issues_created,
              'issues_closed_weight': self.issues_closed,
        }
        return str(d)
