from django.shortcuts import render
from github import GithubException
from pygithub_api_integration.models import Repository


def renderingDocs(request, repo_id):

    repo_name = Repository.objects.get(id=repo_id).full_name
    repo = Repository.requestRepo(repo_name)

    contributingFile = getContributingFile(repo)
    licenseFile = getLicenseFile(repo)
    issueTemplate = getIssueTemplate(repo)
    pullRequestTemplate = getPullRequestTemplate(repo)
    conductFile = getCodeConduct(repo)
    readme = getReadme(repo)

    context = {'contributingFile': contributingFile,
               'licenseFile': licenseFile,
               'issueTemplate': issueTemplate,
               'pullRequestTemplate': pullRequestTemplate,
               'conductFile': conductFile,
               'readme': readme,
               'repo_id': repo.id
               }

    return render(request, 'searchDocs.html', context)


def getReadme(repo):

    try:
        readme = repo.get_file_contents("README.md")
    except GithubException:
        readme = None

    return readme


def getContributingFile(repo):

    try:
        contributingFile = repo.get_file_contents(".github/CONTRIBUTING.md")
    except GithubException:
        contributingFile = None

    return contributingFile


def getCodeConduct(repo):

    try:
        conductFile = repo.get_file_contents(".github/CODE_OF_CONDUCT.md")
    except GithubException:
        conductFile = None
    return conductFile


def getLicenseFile(repo):

    try:
        licenseFile = repo.get_file_contents("LICENSE")
    except GithubException:
        licenseFile = None
    return licenseFile


def getIssueTemplate(repo):

    try:
        issueTemplate = repo.get_file_contents(".github/ISSUE_TEMPLATE.md")
    except GithubException:
        issueTemplate = None
    return issueTemplate


def getPullRequestTemplate(repo):

    way_doc = ".github/PULL_REQUEST_TEMPLATE.md"

    try:
        pullRequestTemplate = repo.get_file_contents(way_doc)
    except GithubException:
        pullRequestTemplate = None
    return pullRequestTemplate
