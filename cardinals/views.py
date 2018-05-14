from django.shortcuts import render
# from pygithub_api_integration.models import Repository


def index(request):

    if request.method == 'POST':
        full_name_repo = request.POST['full_name_repo']

        return full_name_repo

    return render(request, 'index.html')
