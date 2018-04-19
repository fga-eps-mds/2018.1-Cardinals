from github import Github
from django.shortcuts import render
from github import GithubException
from oauth.credentials import get_credentials

username, password = get_credentials()

# Create your views here.
def renderingDocs(request):
    contributingFile = getContributingFile()
    licenseFile = getLicenseFile()

    return render(request, 'searchDocs.html', {'contributingFile': contributingFile,
                                               'licenseFile': licenseFile
                                              })

def getContributingFile():

    g = Github(username, password)
    org = g.get_organization('fga-gpp-mds')
    repo = org.get_repo('2018.1-Cardinals')
    try:
        contributingFile = repo.get_file_contents(".github/CONTRIBUTING.md")
    except GithubException:
        contributingFile =''

    return contributingFile

def getLicenseFile():

    g = Github(username, password)
    org = g.get_organization('fga-gpp-mds')
    repo = org.get_repo('2018.1-Cardinals')
    try:
        licenseFile = repo.get_file_contents("LICENSE")
    except GithubException:
        licenseFile =''
    return licenseFile
