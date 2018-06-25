from django.shortcuts import render
from github import GithubException
from pygithub_api_integration.models import Repository

paths = ["docs/", ".github/", ""]


def renderingDocs(request, organization, repository):
    repo_name = organization + '/' + repository
    repo = Repository.requestRepo(repo_name)

    contributingFile = getContributingFile(repo)
    licenseFile = getLicenseFile(repo)
    issueTemplate = getIssueTemplate(repo)
    pullRequestTemplate = getPullRequestTemplate(repo)
    conductFile = getCodeConduct(repo)
    readme = getReadme(repo)
    repo_id = repo.id

    context = {'contributingFile': contributingFile,
               'licenseFile': licenseFile,
               'issueTemplate': issueTemplate,
               'pullRequestTemplate': pullRequestTemplate,
               'conductFile': conductFile,
               'readme': readme,
               'repo_id': repo_id
               }

    return render(request, 'searchDocs.html', context)


def getReadme(repo):

    try:
        readme = repo.get_readme()

    except GithubException:
        readme = None

    return readme


def getContributingFile(repo):

    contributing_file = None
    i = 0
    while contributing_file is None and i <= 2:
        try:
            contributing_file = repo.get_file_contents(paths[i] +
                                                       "CONTRIBUTING.md")

        except GithubException:
            contributing_file = None

        i += 1

    return contributing_file


def getCodeConduct(repo):

    conduct_file = None
    i = 0
    while conduct_file is None and i <= 2:
        try:
            conduct_file = repo.get_file_contents(paths[i] +
                                                  "CODE_OF_CONDUCT.md")
        except GithubException:
            conduct_file = None

        i += 1

    return conduct_file


def getLicenseFile(repo):

    try:
        license_file = repo.get_license()

    except GithubException:
        license_file = None

    return license_file


def getIssueTemplate(repo):

    template_issue = None
    i = 0
    while template_issue is None and i <= 2:
        try:
            template_issue = repo.get_file_contents(paths[i] +
                                                    "ISSUE_TEMPLATE.md")
        except GithubException:
            template_issue = None

        i += 1

    return template_issue


def getPullRequestTemplate(repo):

    template_pr = None
    i = 0
    while template_pr is None and i <= 2:
        try:
            template_pr = repo.get_file_contents(paths[i] +
                                                 "PULL_REQUEST_TEMPLATE.md")
        except GithubException:
            template_pr = None

        i += 1

    return template_pr
