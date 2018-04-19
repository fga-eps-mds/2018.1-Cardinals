from github import Github
from django.shortcuts import render
from github import GithubException
from oauth.credentials import get_credentials

username, password = get_credentials()

# Create your views here.
def renderingDocs(request):
    contributingFile = getContributingFile()
    licenseFile = getLicenseFile()
    issueTemplate = getIssueTemplate()
    pullRequestTemplate = getPullRequestTemplate()
    conductFile = getCodeConduct()
    readme = getReadme()

    return render(request, 'searchDocs.html', {'contributingFile': contributingFile,
                                               'licenseFile': licenseFile,
                                               'issueTemplate': issueTemplate,
                                               'pullRequestTemplate': pullRequestTemplate,
                                               'conductFile' : conductFile,
                                               'readme' : readme
                                              })

def getReadme():

    g = Github(username, password)
    org = g.get_organization('fga-gpp-mds')
    repo = org.get_repo('2018.1-Cardinals')
    try:
        readme = repo.get_file_contents("README.md")
    except GithubException:
        readme =''

    return readme


def getContributingFile():

    g = Github(username, password)
    org = g.get_organization('fga-gpp-mds')
    repo = org.get_repo('2018.1-Cardinals')
    try:
        contributingFile = repo.get_file_contents(".github/CONTRIBUTING.md")
    except GithubException:
        contributingFile =''

    return contributingFile

def getCodeConduct():

    g = Github(username, password)
    org = g.get_organization('fga-gpp-mds')
    repo = org.get_repo('2018.1-Cardinals')
    try:
        conductFile = repo.get_file_contents(".github/CODE_OF_CONDUCT.md")
    except GithubException:
        conductFile =''
    return conductFile

def getLicenseFile():

    g = Github(username, password)
    org = g.get_organization('fga-gpp-mds')
    repo = org.get_repo('2018.1-Cardinals')
    try:
        licenseFile = repo.get_file_contents("LICENSE")
    except GithubException:
        licenseFile =''
    return licenseFile

def getIssueTemplate():

    g = Github(username, password)
    org = g.get_organization('fga-gpp-mds')
    repo = org.get_repo('2018.1-Cardinals')
    try:
        issueTemplate = repo.get_file_contents(".github/ISSUE_TEMPLATE.md")
    except GithubException:
        issueTemplate =''
    return issueTemplate

def getPullRequestTemplate():

    g = Github(username, password)
    org = g.get_organization('fga-gpp-mds')
    repo = org.get_repo('2018.1-Cardinals')
    try:
        pullRequestTemplate = repo.get_file_contents(".github/PULL_REQUEST_TEMPLATE.md")
    except GithubException:
        pullRequestTemplate =''
    return pullRequestTemplate