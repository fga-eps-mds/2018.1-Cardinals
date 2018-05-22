from django.shortcuts import render, redirect
from github import Github
from github import GithubException as GE
from index.views import searchRepository
from oauth.credentials import get_credentials
from django.contrib import messages
from . import constants


def getContributors(repo):

    contributors = repo.get_contributors()

    return contributors

def getRepoInfo(request):

    username, password = get_credentials()

    repo_name = (searchRepository(request).content).decode('utf-8')

    try:
        git = Github(username, password)
        repo = git.get_repo(repo_name)

        contributors = getContributors(repo)
        context = {"repo": repo, "contributors": contributors}

        return render(request, 'repository_info.html', context)

    except GE:
        messages.add_message(
            request,
            messages.ERROR,
            constants.INVALID_REPOSITORY_MESSAGE,
        )
        # message = 'Insira um repositório válido!'
        return redirect('index')
