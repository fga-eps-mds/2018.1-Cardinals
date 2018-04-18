from github import Github
from django.shortcuts import render
from github import GithubException

# Create your views here.
def getContributingFile(request):

    g = Github("mdscardinals", "(cardinals1)")
    org = g.get_organization('fga-gpp-mds')
    repo = org.get_repo('2018.1-Cardinals')
    try:
        contributingFile = repo.get_file_contents(".github/CONTRIBUTING.md")
    except GithubException:
        contributingFile =''

    return render(request, 'searchDocs.html', {"contributingFile": contributingFile})

def getLicenseFile(request):

    g = Github("mdscardinals", "(cardinals1)")
    org = g.get_organization('fga-gpp-mds')
    repo = org.get_repo('2018.1-Cardinals')
    licenseFile = repo.get_license()

    return render(request, 'searchDocs.html', {"licenseFile":licenseFile})