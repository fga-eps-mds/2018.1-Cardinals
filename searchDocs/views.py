from github import Github
from django.shortcuts import render
from github import GithubException
from oauth.credentials import get_credentials

def setup_repository_if_none(request):
    global username, password, g, org, repo

    if 'username' not in request.session:
        username, password = get_credentials()
        g = Github(username, password)
        org = g.get_organization('fga-gpp-mds')
        repo = org.get_repo('2018.1-Cardinals')
        request.session['username'] = username


paths = ["docs/", ".github/", ""]

def renderingDocs(request):
    setup_repository_if_none(request)

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
        readme = repo.get_readme()
    except GithubException:
        readme = None

    return readme


def getContributingFile():

    contributingFile = None
    i = 0
    while contributingFile is None and i <= 2:
        try:
            contributingFile = repo.get_file_contents(paths[i] + "CONTRIBUTING.md")
                    
        except GithubException:
            contributingFile = None

        i += 1

    return contributingFile


def getCodeConduct():
    
    conductFile = None
    i=0
    while conductFile is None and i <= 2:
        try:
            conductFile = repo.get_file_contents(paths[i] + "CODE_OF_CONDUCT.md")
        except GithubException:
            conductFile = None

        i += 1
    return conductFile


def getLicenseFile():

    try:
        licenseFile = repo.get_license()
    except GithubException:
        licenseFile = None
    return licenseFile


def getIssueTemplate():

    issueTemplate = None
    i =0
    while issueTemplate is None and i <= 2:
        try:
            issueTemplate = repo.get_file_contents(paths[i] + "ISSUE_TEMPLATE.md")
        except GithubException:
            issueTemplate = None

        i += 1
    return issueTemplate


def getPullRequestTemplate():

    pullRequestTemplate = None
    i =0

    while pullRequestTemplate is None and i <= 2:
        try:
            pullRequestTemplate = repo.get_file_contents(paths[i] + "PULL_REQUEST_TEMPLATE.md")
        except GithubException:
            pullRequestTemplate = None

        i += 1
    return pullRequestTemplate
