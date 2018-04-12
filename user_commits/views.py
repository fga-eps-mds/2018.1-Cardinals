from github import Github
from django.shortcuts import render
from datetime import datetime

def user_commits(request):
    
    g = Github("mdscardinals", "(cardinals1)")

    org = g.get_organization('fga-gpp-mds')
    repo = org.get_repo('2018.1-Cardinals')      

    allCommits = repo.get_stats_contributors()

    

    return render(request, 'user_commits.html', {"allCommits" : allCommits})

