from django.db import models
from github import Github
from oauth.credentials import get_credentials


class Repository(models.Model):

    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)

    def requestRepo(repo_name, username=None, password=None):

        if (username is None) and (password is None):

            username, password = get_credentials()
            git = Github(username, password)
            repo = git.get_repo(repo_name)

        else:
            pass

        return repo


class Contributor(models.Model):

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    login = models.CharField(max_length=255)
    commits = models.IntegerField(null=True)
    line_code = models.IntegerField(null=True)
    issues_created = models.IntegerField(null=True)
    issues_closed = models.IntegerField(null=True)
    score = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    repository = models.ManyToManyField(Repository)

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
            for c in contributors:
                c.score = round(float(c.commits +
                                      Contributor.getPercent(c.line_code,
                                                             line_code_repo) +
                                      c.issues_created +
                                      c.issues_closed), 2)
                c.save()

        else:
            for c in contributors:
                c.score = round(float(c.commits * int(weight["commit"]) +
                                      Contributor.getPercent(c.line_code,
                                                             line_code_repo) *
                                      int(weight["line_code"]) +
                                      c.issues_created *
                                      int(weight["issues_created"]) +
                                      c.issues_closed *
                                      int(weight["issues_closed"])), 2)

        return contributors


# class ContributingWeek(models.Model):

#     line_add = models.IntegerField()
#     line_deletion = models.IntegerField()
#     total_commits = models.IntegerField()
#     contributor = models.ForeignKey('Contributor',
#                                     on_delete=models.CASCADE)


# class Commit(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     created_at = models.DateTimeField()
#     repository = models.ForeignKey('Repository',
#                                    on_delete=models.CASCADE)


class Issue(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_by = models.BigIntegerField()  # ID of creator contributor
    closed_by = models.BigIntegerField(null=True)  # ID of closing contributor
    state = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    closed_at = models.DateTimeField(null=True)
    repository = models.ForeignKey('Repository',
                                   on_delete=models.CASCADE)

    def requestIssues(repo_request, repo):

        issues_all = repo_request.get_issues(state="all")

        for i in issues_all:
            issue = Issue()
            issue.id = i.id
            issue.created_by = i.user.id
            if i.closed_by is not None:
                issue.closed_by = i.closed_by.id
            issue.state = i.state
            issue.created_at = i.created_at
            issue.closed_at = i.closed_at
            issue.id_repository = repo
            issue.save()
