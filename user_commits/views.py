from github import Github
from django.shortcuts import render
from index.views import searchRepository
from oauth.credentials import get_credentials
from datetime import datetime

allCommits = []

def getCommits(request):
    return render(request, 'commits.html')

def getResultCommits(request):
    if request.method == 'GET':
        novaLista = list(allCommits)

        if request.GET['dataInicio'] != "":
            dataInicio = datetime.strptime(request.GET['dataInicio'], "%Y-%m-%d")
            data = datetime(dataInicio.year, dataInicio.month, dataInicio.day)
            for commit in novaLista:
                if commit.commit.author.date <= data:
                    novaLista.remove(commit)
        if request.GET['dataFinal'] != "":
            dataFinal = datetime.strptime(request.GET['dataFinal'], "%Y-%m-%d")
            data = datetime(dataFinal.year, dataFinal.month, dataFinal.day)
            for commit in novaLista:
                if commit.commit.author.date >= data:
                    novaLista.remove(commit)
        
        return render(request, 'user_commits.html',{"commits_novalista": novaLista})

    elif request.method == 'POST':
        repository = request.POST['repository']
        username, password = get_credentials()
        git = Github(username, password)
        repo = git.get_repo(repository)
        for commit in repo.get_commits():
            allCommits.append(commit)

        return render(request, 'user_commits.html',{"commits": allCommits})
        