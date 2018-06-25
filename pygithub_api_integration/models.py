from django.db import models
from operator import attrgetter
from github import Github
from oauth.credentials import get_credentials


def certify_request(return_function):

    obj_request = None

    while obj_request is None:
        obj_request = return_function

    return obj_request


class Repository(models.Model):

    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)

    def requestRepo(repo_name):

        username, password = get_credentials()
        git = Github(username, password)

        repo_request = certify_request(git.get_repo(repo_name))

        return repo_request

    def saveRepo(repo_request):
        Repository.objects.filter(full_name=repo_request.full_name).delete()

        repo = Repository()
        repo.full_name = repo_request.full_name
        repo.name = repo_request.name

        repo.save()

        return repo


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

    def requestContributors(repo_request):

        contr_request = certify_request(repo_request.get_stats_contributors())

        return contr_request

    def saveContributors(contributors_request, repo):

        for contrib in contributors_request:
            contributor = Contributor()
            contributor.id = contrib.author.id
            contributor.name = contrib.author.name
            contributor.login = contrib.author.login
            contributor.email = contrib.author.email
            contributor.commits = contrib.total

            contributor.save()
            contributor.repository.add(repo)
            ContributingWeek.saveContributingWeek(contrib, contributor)

    def setLineCodeContrib(contributors):

        for contrib in contributors:
            line_code = 0
            weeks = ContributingWeek.objects.filter(contributor=contrib.id)
            for week in weeks:
                line_code += week.line_add + week.line_del

            contrib.line_code = line_code
            contrib.save()

    def setIssuesCreatedFor(contributors, repo_id):

        for contrib in contributors:
            num_issues_created = 0
            issues_all = Issue.objects.filter(repository=repo_id)
            for issue in issues_all:
                if issue.created_by == contrib.id:
                    num_issues_created += 1

            contrib.issues_created = num_issues_created
            contrib.save()

    def setIssuesClosedFor(contributors, repo_id):

        for contrib in contributors:
            num_issues_closed = 0
            issues_all = Issue.objects.filter(repository=repo_id)
            for issue in issues_all:
                if issue.state == "closed" and issue.closed_by == contrib.id:
                        num_issues_closed += 1

            contrib.issues_closed = num_issues_closed
            contrib.save()

    def getLineCodeRepo(contributors):

        line_code_repo = 0

        for contrib in contributors:
            line_code_repo += contrib.line_code

        return line_code_repo

    def getPercent(line_code, line_code_repo):

        percent = (line_code * 100) / line_code_repo

        return percent

    def getScore(contributors, weight=None):

        line_code_repo = Contributor.getLineCodeRepo(contributors)

        if weight is None:
            for contrib in contributors:
                contrib.score = round(float(contrib.commits +
                                      Contributor.getPercent(contrib.line_code,
                                                             line_code_repo) +
                                      contrib.issues_created +
                                      contrib.issues_closed), 2)
                contrib.save()

        else:
            for contrib in contributors:
                contrib.score = round(float(contrib.commits *
                                      int(weight.commit) +
                                      Contributor.getPercent(contrib.line_code,
                                                             line_code_repo) *
                                      int(weight.line_code) +
                                      contrib.issues_created *
                                      int(weight.issues_created) +
                                      contrib.issues_closed *
                                      int(weight.issues_closed)), 2)

        ranking_commiters = sorted(contributors,
                                   key=attrgetter('score'),
                                   reverse=True)

        return ranking_commiters


class ContributingWeek(models.Model):

    week = models.CharField(max_length=255)
    line_add = models.IntegerField()
    line_del = models.IntegerField()
    commits = models.IntegerField()
    contributor = models.ForeignKey('Contributor',
                                    on_delete=models.CASCADE)

    def saveContributingWeek(contributor_request, contributor):

        weeks = certify_request(contributor_request.weeks)

        for week in weeks:
            contrib_week = ContributingWeek()
            contrib_week.week = week.w
            contrib_week.line_add = week.a
            contrib_week.line_del = week.d
            contrib_week.commits = week.c
            contrib_week.contributor = contributor
            contrib_week.save()


class Commit(models.Model):
    sha = models.CharField(max_length=255, primary_key=True)
    date = models.DateTimeField()
    message = models.TextField(null=True)
    repository = models.ForeignKey('Repository',
                                   on_delete=models.CASCADE)
    author = models.ForeignKey('Contributor',
                               on_delete=models.CASCADE)

    def requestCommit(repo_request):

        commit_request = certify_request(repo_request.get_commits())

        return commit_request

    def saveCommit(commit_request, repo, contributors):

        for commit_r in commit_request:
            commit = Commit()
            commit.sha = commit_r.sha
            commit.date = commit_r.commit.author.date
            commit.message = commit_r.commit.message
            commit.repository = repo
            for contrib in contributors:
                if commit_r.author.id == contrib.id:
                    commit.author = contrib
            commit.save()


class Issue(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_by = models.BigIntegerField()  # ID of creator contributor
    closed_by = models.BigIntegerField(null=True)  # ID of closing contributor
    state = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    closed_at = models.DateTimeField(null=True)
    repository = models.ForeignKey('Repository',
                                   on_delete=models.CASCADE)

    def requestIssues(repo_request):

        issues_request = certify_request(repo_request.get_issues(state="all"))

        return issues_request

    def saveIssues(issues_request, repo):

        for issue_r in issues_request:
            issue = Issue()
            issue.id = issue_r.id
            issue.created_by = issue_r.user.id
            if issue_r.closed_by is not None:
                issue.closed_by = issue_r.closed_by.id
            issue.state = issue_r.state
            issue.created_at = issue_r.created_at
            issue.closed_at = issue_r.closed_at
            issue.repository = repo
            issue.save()
