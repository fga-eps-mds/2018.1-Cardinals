from django.db import models


class Repository(models.Model):

    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    # update handling attributes
    events_url = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)


class Contributor(models.Model):

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=254, null=True)
    login = models.CharField(max_length=255)
    commits = models.IntegerField(default=0, null=True)
    line_code = models.IntegerField(default=0, null=True)
    issues_created = models.IntegerField(default=0, null=True)
    issues_closed = models.IntegerField(default=0, null=True)
    score = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    repository = models.ManyToManyField(Repository)


class ContributingWeek(models.Model):

    week = models.CharField(max_length=255)
    line_add = models.IntegerField()
    line_del = models.IntegerField()
    commits = models.IntegerField()
    contributor = models.ForeignKey('Contributor',
                                    on_delete=models.CASCADE)


class Commit(models.Model):
    sha = models.CharField(max_length=255, primary_key=True)
    date = models.DateTimeField()
    message = models.TextField(null=True)
    repository = models.ForeignKey('Repository',
                                   on_delete=models.CASCADE)
    author = models.ForeignKey('Contributor',
                               on_delete=models.CASCADE)



class Issue(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_by = models.BigIntegerField()  # ID of creator contributor
    closed_by = models.BigIntegerField(null=True)  # ID of closing contributor
    state = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    closed_at = models.DateTimeField(null=True)
    repository = models.ForeignKey('Repository',
                                   on_delete=models.CASCADE)

