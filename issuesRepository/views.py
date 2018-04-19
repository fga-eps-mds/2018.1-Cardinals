from django.shortcuts import render
from github import Github,InputFileContent
from index.views import searchRepository
from oauth.credentials import get_credentials
from datetime import datetime
myRepository = ""
allIssues = []

def getIssues(request):
    return render(request, 'issues.html')

def getResultIssues(request):
    dataInicio = " "
    repository = " "
    if request.method == 'GET':
        novaLista = list(allIssues)

        if request.GET['states'] != "all":
            opcoes = request.GET['states']
            for issue in allIssues:
                if issue.state != opcoes:
                    novaLista.remove(issue)

                if request.GET['dataInicio'] != "":
                    dataInicio = datetime.strptime(request.GET['dataInicio'], "%Y-%m-%d")
                    data = datetime(dataInicio.year, dataInicio.month, dataInicio.day)
                    for issue in novaLista:
                        if issue.created_at >= data:
                            novaLista.remove(issue)
                
        else:
            for issue in allIssues:
                novaLista.append(issue)

                if request.GET['dataInicio'] != "":
                    dataInicio = datetime.strptime(request.GET['dataInicio'], "%Y-%m-%d")
                    data = datetime(dataInicio.year, dataInicio.month, dataInicio.day)
                    for issue in novaLista:
                        if issue.created_at >= data:
                            novaLista.remove(issue)
        
        return render(request, 'resultsIssues.html',{"issues": novaLista})

    elif request.method == 'POST':
        repository = "fga-gpp-mds/2018.1-Cardinals"
        username, password = get_credentials()
        myRepository = repository
        git = Github(username, password)
        repo = git.get_repo(repository)
        for issue in repo.get_issues(state="all"):
            allIssues.append(issue)

        return render(request, 'resultsIssues.html',{"issues": allIssues})

