from github import GitHub
from django.shortcuts import render
from index.views import searchRepository
from oauth.credentials import get_credentials 
from datetime import datetime


def verify_readme(repo):
    read = repo.get_readme()

    return read

def getReadme(request):

    username , password = get_credentials()
    repo_name = ('fga-gpp-mds/2018.1-Cardinals')

    git = GitHub(username, password)
    repo = git.get_repo(repo_name)

    read = verify_readme(repo)
     
    return render(request, 'readme_doc.html', {"read": read})