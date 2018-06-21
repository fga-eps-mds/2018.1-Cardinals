from api.models import Repository, Contributor
from github import Github
from github import GithubException
from collections import Counter, defaultdict

import requests
from datetime import datetime, timedelta
from github_api.credentials import get_credentials
import re


username, password = get_credentials()
git = Github(username, password)

## Github Access and Model update
def get_github_repository(name):
    repo = get_repo_db(name)
    if repo:
        if is_updated(repo) == False:
            update_repository(repo)
        else:
            print("repository up to date")
    else:
        print("INVALID repository")
        return None
    return repo

def get_repo_github(org_name,repo_name):
    org = git.get_organization(org_name)
    repo = org.get_repo(repo_name)
    return repo


def get_repo_db(full_name):
    obj = None
    
    try: 
        obj = Repository.objects.get(full_name=full_name)
    except Repository.DoesNotExist:
        obj = create_new_repository(full_name)
        if obj:
            obj.save()
    return obj

def create_new_repository(full_name):
    array_full_name = re.split("/",full_name)

    org_name = array_full_name[0]
    repo_name = array_full_name[1]

    github_repo = get_repo_github(org_name,repo_name)

    if github_repo == None:
        return None

    events = github_repo.get_events()
    last_event = events[0]

    new_model_repo = Repository()
    new_model_repo.full_name = github_repo.full_name
    new_model_repo.name = repo_name
    new_model_repo.updated_at = last_event.created_at
    new_model_repo.events_url = github_repo.events_url
    new_model_repo.save()

    # Updating contributors
    update_contributors(github_repo, new_model_repo)

    return new_model_repo

def is_updated(repository):
    last_date = get_last_event_date(repository)

    if not repository.updated_at or last_date > repository.updated_at:
        return False
    else:
        return True

def update_repository(repo):
    full_name = repo.full_name

    array_full_name = re.split("/",full_name)

    org_name = array_full_name[0]
    repo_name = array_full_name[1]

    github_repo = get_repo_github(org_name,repo_name)
    last_event = github_repo.get_events()[0]
    
    repo.updated_at = last_event.created_at
    repo.events_url = github_repo.events_url

    repo.save()
    print("Repository updated!")

    # Updating contributors
    update_contributors(github_repo, repo)


def get_last_event_date(repository):
    if not repository.events_url:
        return datetime(1,1,1)

    req = requests.get(repository.events_url)
    last_date_unicode = req.json()[0]['created_at']
    last_date = datetime.strptime(last_date_unicode, '%Y-%m-%dT%H:%M:%SZ')
    return last_date

def update_contributors(github_repo, repository):
    contributors_request = Contributor.requestContributors(github_repo)
    Contributor.saveContributors(contributors_request, repository)


def get_commits_chart_data(full_name):
    # repository_url = organization + '/' + repository
    github = Github(username, password)
    repository = github.get_repo(full_name)

    all_commit_count = defaultdict(list)
    signed_commit_count = Counter()

    for commit in repository.get_commits():
        real_date = commit.commit.author.date - timedelta(hours=2)
        all_commit_count[real_date.date()].append(commit.commit)
        if (commit.commit.message.count("Co-authored-by:") > 1 or (commit.commit.message.count("Co-authored-by:") == 1)) or (commit.commit.message.count("Signed-off-by:") > 1 or (commit.commit.message.count("Signed-off-by:") == 1 and
            commit.commit.author.email not in commit.commit.message) or ((commit.commit.author.email != commit.commit.committer.email)
            and ("noreply@github.com" not in commit.commit.committer.email))):

            signed_commit_count[real_date.date()] += 1
        else:
            signed_commit_count[real_date.date()] += 0

    commit_count = {k: len(v) for k, v in all_commit_count.items()}

    dates = list(commit_count.keys())
    dates.sort()

    commit_count = sorted(commit_count.items())
    all_amount_by_date = [x[1] for x in commit_count]
    signed_commit_count = sorted(signed_commit_count.items())
    signed_amount_by_date = [x[1] for x in signed_commit_count]

    return dates, all_amount_by_date, signed_amount_by_date
