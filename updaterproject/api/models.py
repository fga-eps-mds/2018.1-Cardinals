from __future__ import unicode_literals

from django.db import models


class Repository(models.Model):

    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    # update handling attributes
    events_url = models.CharField(max_length=200, null=True)
    updated_at = models.DateTimeField(null=True)

    issues_db_updated = models.IntegerField(default=0, null=False)
    commits_db_updated = models.IntegerField(default=0, null=False)

    def saveRepo(repo_request):

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

    def mock(self):
        contributor = Contributor()
        contributor.id = 123
        contributor.name = 'Robson'
        contributor.login = 'Robson@git'
        contributor.email = 'Robson2003@email.com'
        contributor.commits = '100'
        return contributor


    def requestContributors(repo_request):

        retry = 3
        contributors_request = None
        while(contributors_request == None and retry >= 0):
            retry -= 1
            contributors_request = repo_request.get_stats_contributors()

        return contributors_request

    def saveContributors(contributors_request, repo):

        if not contributors_request:
            return

        for c in contributors_request:
            contributor = Contributor()
            contributor.id = c.author.id
            contributor.name = c.author.name
            contributor.login = c.author.login
            contributor.email = c.author.email
            contributor.commits = c.total

            contributor.save()
            contributor.repository.add(repo)
            ContributingWeek.saveContributingWeek(c, contributor)

    def setLineCodeContrib(contributors):

        for c in contributors:
            line_code = 0
            weeks = ContributingWeek.objects.filter(contributor=c.id)
            for week in weeks:
                line_code += week.line_add + week.line_del

            c.line_code = line_code
            c.save()

    def setIssuesCreatedFor(contributors, repo_id):

        for c in contributors:
            num_issues_created = 0
            issues_all = Issue.objects.filter(repository=repo_id)
            for issue in issues_all:
                if issue.created_by == c.id:
                    num_issues_created += 1

            c.issues_created = num_issues_created
            c.save()

    def setIssuesClosedFor(contributors, repo_id):

        for c in contributors:
            num_issues_closed = 0
            issues_all = Issue.objects.filter(repository=repo_id)
            for issue in issues_all:
                if issue.state == "closed":
                    if issue.closed_by == c.id:
                        num_issues_closed += 1

            c.issues_closed = num_issues_closed
            c.save()

    def getLineCodeRepo(contributors):

        line_code_repo = 0

        for contributor in contributors:
            line_code_repo += contributor.line_code

        return line_code_repo

    def getPercent(line_code, line_code_repo):

        percent = (line_code * 100) / line_code_repo

        return percent

    def getScore(contributors, weight=None):

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
                c.score = round(float(c.commits * int(weight.commit) +
                                      Contributor.getPercent(c.line_code,
                                                             line_code_repo) *
                                      int(weight.line_code) +
                                      c.issues_created *
                                      int(weight.issues_created) +
                                      c.issues_closed *
                                      int(weight.issues_closed)), 2)

        return contributors


class ContributingWeek(models.Model):

    week = models.CharField(max_length=255)
    line_add = models.IntegerField()
    line_del = models.IntegerField()
    commits = models.IntegerField()
    contributor = models.ForeignKey('Contributor',
                                    on_delete=models.CASCADE)

    def saveContributingWeek(contributor_request, contributor):

        weeks = contributor_request.weeks

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

        retry = 3
        commit_request = None
        while(commit_request == None and retry >= 0):
            retry -= 1
            commit_request = repo_request.get_commits()

        return commit_request

    def saveCommit(commit_request, repo, contributors):

        if not commit_request:
            return

        for c in commit_request:
            commit = Commit()
            commit.sha = c.sha
            commit.date = c.commit.author.date
            commit.message = c.commit.message
            commit.repository = repo
            if not c.author:
                continue
            for contrib in contributors:
                if c.author.id == contrib.id:
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

        retry = 3
        issues_request = None
        while(issues_request == None and retry >= 0):
            retry -= 1
            issues_request = repo_request.get_issues(state="all")

        return issues_request

    def saveIssues(issues_request, repo):

        if not issues_request:
            return

        for i in issues_request:
            issue = Issue()
            issue.id = i.id
            issue.created_by = i.user.id
            if i.closed_by is not None:
                issue.closed_by = i.closed_by.id
            issue.state = i.state
            issue.created_at = i.created_at
            issue.closed_at = i.closed_at
            issue.repository = repo
            issue.save()
