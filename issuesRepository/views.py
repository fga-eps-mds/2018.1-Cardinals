from django.shortcuts import render
from github import Github,InputFileContent
from index.views import searchRepository
from datetime import datetime
username = "mdscardinals"
password = "(cardinals1)"
myRepository = ""
allIssues = []

def getIssues(request):
    return render(request, 'issues.html')

def getResultIssues(request):
    dataInicio = " "
    repository = " "
    if request.method == 'GET':
        novaLista = []

        if request.GET['states'] != "all":
            opcoes = request.GET['states']
            for issue in allIssues:
                if issue.state == opcoes:
                    novaLista.append(issue)

                if request.GET['dataInicio'] != "":
                    dataInicio = request.GET['dataInicio']
                    for issue in allIssues:
                        if issue.created_at.date <= datetime(dataInicio):
                            novaLista.remove(issue)
                if request.GET['dataFechamento'] != "":
                    dataFechamento = request.GET['dataFechamento']
                    for issue in allIssues:
                        if issue.closed_at.date >= datetime(dataFechamento):
                            novaLista.remove(issue)
        else:
            for issue in allIssues:
                novaLista.append(issue)

                if request.GET['dataInicio'] != "":
                    dataInicio = request.GET['dataInicio']
                    for issue in allIssues:
                        if issue.created_at.date <= datetime(dataInicio):
                            novaLista.remove(issue)
                if request.GET['dataFechamento'] != "":
                    dataFechamento = request.GET['dataFechamento']
                    for issue in allIssues:
                        if issue.closed_at.date >= datetime(dataFechamento):
                            novaLista.remove(issue)
        
        return render(request, 'resultsIssues.html',{"issues": novaLista})

    elif request.method == 'POST':
        repository = request.POST['repository']

        myRepository = repository
        git = Github(username, password)
        repo = git.get_repo(repository)
        for issue in repo.get_issues(state="all"):
            allIssues.append(issue)

        return render(request, 'resultsIssues.html',{"issues": allIssues})

