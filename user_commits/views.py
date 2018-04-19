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
        myRepository = repository
        git = Github(username, password)
        repo = git.get_repo(repository)
        for commit in repo.get_commits():
            allCommits.append(commit)

        return render(request, 'user_commits.html',{"commits": allCommits})








'''
def getCommitsUser(repo):

    commits_user = repo.get_stats_contributors()

    return commits_user

def getCommitStatuses(repo):

    commit_statuses = repo.get_commits()

    return commit_statuses

def getCommitesDate(request):

    if request.method == 'POST':
        dataInicio = datetime.strptime(request.POST['dataInicio'], "%Y-%m-%d")
        dataFinal = datetime.strptime(request.GET['dataFinal'], "%Y-%m-%d")
        return dataInicio, dataFinal
    else:
        message = '2000-02-01'
        return message


def getResultCommits(request):

    dataInicial = datetime.strptime(getCommitesDate(request), "%Y-%m-%d")
    dataFinal = datetime.strptime(getCommitesDate(request), "%Y-%m-%d")

    username, password = get_credentials()
    repo_name = ('fga-gpp-mds/2018.1-Cardinals')
    #repo_name = searchRepository(request)

    git = Github(username, password)
    repo = git.get_repo(repo_name)

    commits_user = getCommitsUser(repo)
    commit_statuses = getCommitStatuses(repo)

    for i in commit_statuses:
        if i.commit.author.date>=dataInicial and i.commit.author.date<=dataFinal:
            lista = i.commit.author.date, commit.author.name
            print(lista)

    
    return render(request, 'user_commits.html',{"commits_user": commits_user, "commit_statuses": commit_statuses})
'''