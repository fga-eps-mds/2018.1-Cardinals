from django.shortcuts import render, redirect
from github import Github
from github import GithubException as GE
from cardinals.views import index
from oauth.credentials import get_credentials
from django.contrib import messages


def getContributors(repo):

    contributors = repo.get_contributors()

    return contributors


def getRepoInfo(request):

    username, password = get_credentials()

    repo_name = index(request)

    try:
        git = Github(username, password)
        repo = git.get_repo(repo_name)

        contributors = getContributors(repo)

        return render(request, 'repository_info.html',
                      {"repo": repo,
                       "contributors": contributors})

    except GE:
        messages.add_message(
            request,
            messages.ERROR,
            'Insira um repositório válido!'
        )
        # message = 'Insira um repositório válido!'
        return redirect('index')
