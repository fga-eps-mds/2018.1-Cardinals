from django.shortcuts import render
from github import GithubException
from api_request.models import RepositoryAPI


def rendering_docs(request, organization, repository):
    
    repo = RepositoryAPI(organization, repository)

    context = {'contributingFile': repo.contributing_file,
               'licenseFile': repo.license_file,
               'issueTemplate': repo.issue_template,
               'pullRequestTemplate': repo.pull_request_template,
               'conductFile': repo.conduct_file,
               'readme': repo.readme,
               'repo_id': 0
               }

    return render(request, 'searchDocs.html', context)

