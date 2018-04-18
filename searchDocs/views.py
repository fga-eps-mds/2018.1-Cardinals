from github import Github
from django.shortcuts import render

# Create your views here.
def getContributingFile(request):

    g = Github("mdscardinals", "(cardinals1)")
    org = g.get_organization('fga-gpp-mds')
    repo = org.get_repo('2018.1-Cardinals')
    contributingFile = repo.get_contents(".github/ISSUE_TEMPLATE.md")

    return render(request, 'searchDocs.html', {"contributingFile": contributingFile})

# def getLicenses(request):
#
#    g = Github("mdscardinals", "(cardinals1)")
#    org = g.get_organization('fga-gpp-mds')
#    repo = org.get_repo('2018.1-Cardinals')
#    licenseFile = repo.get_licenses()

#    return render(request, 'searchDocs.html', {"licenseFile":licenseFile})