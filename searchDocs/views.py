from django.shortcuts import render
from github import GithubException
from pygithub_api_integration.models import Repository

paths = ["docs/", ".github/", ""]


def rendering_docs(request, organization, repository):
    repo_name = organization + '/' + repository
    repo = Repository.requestRepo(repo_name)

    contributing_file = get_contributing_file(repo)
    license_file = get_license_file(repo)
    issue_template = get_issue_template(repo)
    pull_request_template = get_pull_request_template(repo)
    conduct_file = get_code_conduct(repo)
    readme = get_readme(repo)
    repo_id = repo.id

    context = {'contributingFile': contributing_file,
               'licenseFile': license_file,
               'issueTemplate': issue_template,
               'pullRequestTemplate': pull_request_template,
               'conductFile': conduct_file,
               'readme': readme,
               'repo_id': repo_id
               }

    return render(request, 'searchDocs.html', context)


def check_path(repo, name_file):
    file = None
    i = 0
    while file is None and i <= 2:
        try:
            file = repo.get_file_contents(paths[i] + name_file)

        except GithubException:
            file = None

        i += 1

    return file


def get_readme(repo):

    try:
        readme = repo.get_readme()

    except GithubException:
        readme = None

    return readme


def get_license_file(repo):

    try:
        license_file = repo.get_license()

    except GithubException:
        license_file = None

    return license_file


def get_contributing_file(repo):

    contributing_file = check_path(repo, "CONTRIBUTING.md")

    return contributing_file


def get_code_conduct(repo):

    conduct_file = check_path(repo, "CODE_OF_CONDUCT.md")

    return conduct_file


def get_issue_template(repo):

    template_issue = check_path(repo, "ISSUE_TEMPLATE.md")

    return template_issue


def get_pull_request_template(repo):

    template_pr = check_path(repo, "PULL_REQUEST_TEMPLATE.md")

    return template_pr
