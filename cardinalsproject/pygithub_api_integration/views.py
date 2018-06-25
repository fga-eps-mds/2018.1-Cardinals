from django.shortcuts import render, redirect
from django.contrib import messages
import socket
from . import constants

from api_request.models import RepositoryAPI


def get_repo_info(request, organization, repository):

    try:
        repository = RepositoryAPI(organization, repository)
        context = {"repo": repository, "contributors": repository.contributors}

        return render(request, 'repository_info.html', context)

    except socket.timeout and socket.gaierror:
        messages.add_message(
            request,
            messages.ERROR,
            constants.TIMEOUT_MESSAGE,
        )

        return redirect('index')
