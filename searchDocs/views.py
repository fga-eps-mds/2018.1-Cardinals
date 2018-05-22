from github import Github
from django.shortcuts import render
from github import GithubException
from oauth.credentials import get_credentials


g = org = repo = None


def setup_repository():
    username, password = get_credentials()
    g = Github(username, password)
    org = g.get_organization('fga-gpp-mds')
    repo = org.get_repo('2018.1-Cardinals')


def renderingDocs(request):
    if g is None:
        setup_repository()

    contributingFile = getContributingFile()
    licenseFile = getLicenseFile()
    issueTemplate = getIssueTemplate()
    pullRequestTemplate = getPullRequestTemplate()
    conductFile = getCodeConduct()
    readme = getReadme()

    return render(request, 'searchDocs.html',
                  {'contributingFile': contributingFile,
                   'licenseFile': licenseFile,
                   'issueTemplate': issueTemplate,
                   'pullRequestTemplate': pullRequestTemplate,
                   'conductFile': conductFile,
                   'readme': readme
                   })


def getReadme():

    try:
        readme = repo.get_file_contents("README.md")
    except GithubException:
        readme = None

    return readme


def getContributingFile():

    try:
        contributingFile = repo.get_file_contents(".github/CONTRIBUTING.md")
    except GithubException:
        contributingFile = None

    return contributingFile


def getCodeConduct():

    try:
        conductFile = repo.get_file_contents(".github/CODE_OF_CONDUCT.md")
    except GithubException:
        conductFile = None
    return conductFile


def getLicenseFile():

    try:
        licenseFile = repo.get_file_contents("LICENSE")
    except GithubException:
        licenseFile = None
    return licenseFile


def getIssueTemplate():

    try:
        issueTemplate = repo.get_file_contents(".github/ISSUE_TEMPLATE.md")
    except GithubException:
        issueTemplate = None
    return issueTemplate


def getPullRequestTemplate():

    way_doc = ".github/PULL_REQUEST_TEMPLATE.md"

    try:
        pullRequestTemplate = repo.get_file_contents(way_doc)
    except GithubException:
        pullRequestTemplate = None
    return pullRequestTemplate
