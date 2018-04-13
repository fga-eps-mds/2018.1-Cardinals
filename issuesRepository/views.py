from django.shortcuts import render
from github import Github,InputFileContent
from index.views import searchRepository

username = "mdscardinals"
password = "(cardinals1)"


def getIssues(request):
    return render(request, 'issues.html')

def getResultIssues(request):

    repo_name = searchRepository(request)

    git = Github(username, password)
    repo = git.get_repo(repo_name)
    issues = repo.get_issues()

    return render(request, 'resultsIssues.html',
                  {"issues": issues})
