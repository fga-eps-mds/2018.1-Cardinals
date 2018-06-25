from github_api.credentials import get_credentials
from api.check_community_files import get_docs
from api.models import *

from github import Github
from github import GithubException

from collections import Counter, defaultdict
from datetime import datetime, timedelta

import requests
import threading
import time
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
    repo = None
    try:
        repo = org.get_repo(repo_name)
    except Exception as ex:
        pass
    
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
    
    # when there is no events on repository
    if not events:
        return None

    last_event = events[0]

    new_model_repo = Repository()
    new_model_repo.full_name = github_repo.full_name
    new_model_repo.name = repo_name
    new_model_repo.updated_at = last_event.created_at
    new_model_repo.events_url = github_repo.events_url

    update_documents_check(github_repo, new_model_repo)

    new_model_repo.save()

    # Updating contributors
    lazy_update_repository(github_repo, new_model_repo)

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

    update_documents_check(github_repo, repo)

    repo.save()

    # Updating database secundary models
    lazy_update_repository(github_repo, repo)

    pass

def update_documents_check(repository_github, repository):
    contrib, lic, issue, pr, conduct, readme = get_docs(repository_github)

    repository.contributing_file = contrib
    repository.license_file = lic
    repository.issue_template = issue
    repository.pull_request_template = pr
    repository.conduct_file = conduct
    repository.readme = readme

def get_last_event_date(repository):
    if not repository.events_url:
        return datetime(1,1,1)

    req = requests.get(repository.events_url)
    last_date_unicode = req.json()[0]['created_at']
    last_date = datetime.strptime(last_date_unicode, '%Y-%m-%dT%H:%M:%SZ')
    return last_date

def lazy_update_repository(github_repo, repo):
    update_contributors(github_repo, repo)
    run_in_background(update_commits, github_repo, repo)
    run_in_background(update_issues, github_repo, repo)
    run_in_background(update_pullrequests, github_repo, repo)

def update_contributors(github_repo, repository):
    print (" -- updating contributors")
    contributors_request = Contributor.requestContributors(github_repo)
    
    if not contributors_request:
        print(" Error: could not find contributors")
        return

    Contributor.saveContributors(contributors_request, repository)
    print (" -- contributors updated")
    update_contributors_scores(repository.id)

def update_commits(github_repo, repository):
    print (" -- updating commits")
    repository.commits_db_updated = 0
    repository.save() # update repository info
    request = Commit.requestCommit(github_repo)
    if not request:
        print(" Error: could not find commits")
        return
    contributors = Contributor.objects.filter(repository__full_name__contains=repository.full_name) 
    Commit.saveCommit(request, repository, contributors)
    repository.commits_db_updated = 1
    repository.save() # update repository info
    print (" -- commits updated")
    update_contributors_scores(repository.id)

def update_pullrequests(github_repo, repository):
    print (" -- updating pullrequests")
    repository.pulls_db_updated = 0
    repository.save() # update repository info
    request = PullRequest.requestPR(github_repo)
    if not request:
        print(" Error: could not find pr")
        return
    PullRequest.savePR(request, repository)
    repository.pulls_db_updated = 1
    repository.save() # update repository info
    print (" -- pullrequests updated")
    update_contributors_scores(repository.id)

def update_issues(github_repo, repository):
    print (" -- updating issues")
    repository.issues_db_updated = 0
    repository.save() # update repository info
    request = Issue.requestIssues(github_repo)
    if not request:
        print(" Error: could not find issues")
        return
    Issue.saveIssues(request, repository)
    repository.issues_db_updated = 1
    repository.save() # update repository info
    print (" -- issues updated")
    update_contributors_scores(repository.id)

def run_in_background( action, github_repo, repository):
    thread = threading.Thread(target=action, args=(github_repo, repository,))
    thread.daemon = True
    thread.start()
    pass


def get_commits_from_repository(full_name):
    github = Github(username, password)
    repository = github.get_repo(full_name)
    return repository.get_commits()

def update_contributors_scores(repo_id):
    commiters = Contributor.objects.filter(repository=repo_id)

    Contributor.setLineCodeContrib(commiters)
    Contributor.setIssuesCreatedFor(commiters, repo_id)
    Contributor.setIssuesClosedFor(commiters, repo_id)

def get_commits_chart_data(full_name):
    all_commits = Commit.objects.filter(repository__full_name__contains=full_name).order_by("date")

    commits_count = Counter()
    paired_count = Counter()

    for commit in all_commits:
        simplified_date = commit.date.strftime('%d-%m-%Y')

        commits_count[simplified_date] += 1

        if commit.paired:
            paired_count[simplified_date] += 1
        else:
            paired_count[simplified_date] += 0

    dates = list(commits_count.keys())
    dates.sort()

    return dates, commits_count.values(), paired_count.values()
