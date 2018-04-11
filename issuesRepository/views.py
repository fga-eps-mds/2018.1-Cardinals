from django.shortcuts import render
from github import Github,InputFileContent

username = "mdscardinals"
password = "(cardinals1)"


def getIssues(request):
    git = Github()
    repos = org.get_repo('fga-gpp-mds/2018.1-Cardinals')
    issuesRepository = []

    user = InputFileContent('Nome')

    for i in repos.get_issues():
        issuesRepository.append(i)

    return render(request, 'issues.html', {"issues": issuesRepository, "campo" : user})
