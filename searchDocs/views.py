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


def checkPath(repo, name_file):
    file = None
    i = 0
    while file is None and i <= 2:
        try:
            file = repo.get_file_contents(paths[i] + name_file)

        except GithubException:
            file = None

        i += 1

    return file


def getReadme(repo):

    try:
        readme = repo.get_readme()

    except GithubException:
        readme = None

    return readme


def getLicenseFile(repo):

    try:
        license_file = repo.get_license()

    except GithubException:
        license_file = None

    return license_file


def getContributingFile(repo):

    contributing_file = checkPath(repo, "CONTRIBUTING.md")

    return contributing_file


def getCodeConduct(repo):

    conduct_file = checkPath(repo, "CODE_OF_CONDUCT.md")

    return conduct_file


def getIssueTemplate(repo):

    template_issue = checkPath(repo, "ISSUE_TEMPLATE.md")

    return template_issue


def getPullRequestTemplate(repo):

    template_pr = checkPath(repo, "PULL_REQUEST_TEMPLATE.md")

    return template_pr
