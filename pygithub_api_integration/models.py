from django.db import models


class Repository(models.Model):

    # id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, null=False)


class Commit(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_at = models.DateTimeField()
    id_repository = models.ForeignKey('Repository',
                                      on_delete=models.CASCADE)


class Contributor(models.Model):

    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255, null=False)
    repositories = models.ManyToManyField(Repository)
    score = models.IntegerField()
    # commits = models.ManyToManyField(Commit)


class ContributingWeek(models.Model):

    line_add = models.IntegerField()
    line_deletion = models.IntegerField()
    total_commits = models.IntegerField()
    id_contributor = models.ForeignKey('Contributor',
                                       on_delete=models.CASCADE)


class Issue(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_by = models.BigIntegerField()  # ID of creator contributor
    closed_by = models.BigIntegerField()  # ID of closing contributor
    is_closed = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    closed_at = models.DateTimeField()
    id_repository = models.ForeignKey('Repository',
                                      on_delete=models.CASCADE)
