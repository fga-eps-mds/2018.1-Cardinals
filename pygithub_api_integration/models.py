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
            repo_request = git.get_repo(repo_name)

        else:
            pass

        return repo_request

    def saveRepo(repo_request):

        repo = Repository()
        repo.full_name = repo_request.full_name
        repo.name = repo_request.name

        repo.save()

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

    def requestContributors(repo_request):

        contributors_request = repo_request.get_stats_contributors()

        return contributors_request

    def saveContributors(contributors_request, repo):

        for c in contributors_request:
            contributor = Contributor()
            contributor.id = c.author.id
            contributor.name = c.author.name
            contributor.login = c.author.login
            contributor.commits = c.total

            contributor.save()
            contributor.repository.add(repo)

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


class Commit(models.Model):
    sha = models.CharField(max_length=255, primary_key=True)
    date = models.DateTimeField()
    repository = models.ForeignKey('Repository',
                                   on_delete=models.CASCADE)
    author = models.ManyToManyField(Contributor)

    def requestCommit(repo_request):

        commit_request = repo_request.get_commits()

        return commit_request

    def saveCommit(commit_request, repo, contributors):

        for c in commit_request:
            commit = Commit()
            commit.sha = c.sha
            commit.date = c.commit.author.date
            commit.repository = repo

            commit.save()
            for cont in contributors:
                if c.author.id == cont.id:
                    commit.author.add(cont)


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

        issues_request = repo_request.get_issues(state="all")

        return issues_request

    def seveIssues(issues_request, repo):

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
