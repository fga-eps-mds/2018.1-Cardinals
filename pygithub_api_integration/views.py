from django.shortcuts import render
#from github import Github
# from github import GithubException

username = "Mateusas3s"
password = "123qaz.;/"
repo = '2018.1-Cardinals'

'''
def request_oauth_token(username, password, repo):

    try:
        git = Github(username, password)
        user = git.get_user()
        auth = user.create_authorization(scopes="public_repo", note=repo)
        return auth.token
    except GithubException as e:
        msg_error = "ERROR: " + str(e)
        return msg_error
'''


def getRepo(request):

    # token = request_oauth_token(username, password, repo)

    git = Github(username, password)
    # git = Github(token)
    user = git.get_user()
    repos = user.get_repos()

    return render(request, 'repos.html',
                  {"repos": repos})


def getContributors(request):

    # token = request_oauth_token
    git = Github(username, password)
    org = git.get_organization('fga-gpp-mds')
    repo = org.get_repo('2018.1-Cardinals')
    contributors = repo.get_contributors()

    return render(request, 'contributors.html',
                  {"contributors": contributors})
