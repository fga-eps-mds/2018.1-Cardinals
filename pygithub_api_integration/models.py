from django.db import models


class Repository(models.Model):

    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)


# class Commit(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     created_at = models.DateTimeField()
#     id_repository = models.ForeignKey('Repository',
#                                       on_delete=models.CASCADE)


class Contributor(models.Model):

    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    commits = models.IntegerField()
    line_code = models.IntegerField()
    issues_created = models.IntegerField()
    issues_closed = models.IntegerField()
    score = models.DecimalField(max_digits=9, decimal_places=2)
    # repository = models.ManyToManyField(Repository)
    # commits = models.ManyToManyField(Commit)

    def getLineCodeRepo(contributors):

        line_code_repo = 0

        for contributor in contributors:
            line_code_repo += contributor.line_code

        return line_code_repo

    def getPercent(line_code, line_code_repo):

        percent = (line_code*100)/line_code_repo

        return percent

    def getStatsContributors(weight=None):

        contributors = Contributor.objects.all()

        line_code_repo = Contributor.getLineCodeRepo(contributors)

        if weight is None:
            for contributor in contributors:
                contributor.score = round(float(contributor.commits +
                                                Contributor.getPercent(contributor.line_code, line_code_repo) +
                                                contributor.issues_created +
                                                contributor.issues_closed), 2)
                contributor.save()
        else:
            for contributor in contributors:
                contributor.score = round(float(contributor.commits * int(weight["commit"]) +
                                                Contributor.getPercent(contributor.line_code, line_code_repo) * int(weight["line_code"]) +
                                                contributor.issues_created * int(weight["issues_created"]) +
                                                contributor.issues_closed * int(weight["issues_closed"])), 2)

        return contributors


# class ContributingWeek(models.Model):

#     line_add = models.IntegerField()
#     line_deletion = models.IntegerField()
#     total_commits = models.IntegerField()
#     id_contributor = models.ForeignKey('Contributor',
#                                        on_delete=models.CASCADE)


# class Issue(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     created_by = models.BigIntegerField()  # ID of creator contributor
#     closed_by = models.BigIntegerField()  # ID of closing contributor
#     is_closed = models.BooleanField(default=False)
#     created_at = models.DateTimeField()
#     closed_at = models.DateTimeField()
#     id_repository = models.ForeignKey('Repository',
#                                       on_delete=models.CASCADE)
