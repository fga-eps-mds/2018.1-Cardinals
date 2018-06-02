from api.models import Repository
from github import Github
from github import GithubException

import requests
from datetime import datetime
import re

git = Github('mdscardinals', '(cardinals1)')

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

    repo = get_repo_github(org_name,repo_name)

    if repo == None:
        return None

    events = repo.get_events()
    last_event = events[0]

    new_model_repo = Repository()
    new_model_repo.full_name = repo.full_name
    new_model_repo.name = repo_name
    new_model_repo.updated_at = last_event.created_at
    new_model_repo.events_url = repo.events_url

    return new_model_repo

def is_updated(repository):
    last_date = get_last_event_date(repository)

    if last_date > repository.updated_at:
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


def get_last_event_date(repository):
    req = requests.get(repository.events_url)
    last_date_unicode = req.json()[0]['created_at']
    last_date = datetime.strptime(last_date_unicode, '%Y-%m-%dT%H:%M:%SZ')
    return last_date
