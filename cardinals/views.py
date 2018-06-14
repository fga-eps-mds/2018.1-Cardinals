from django.shortcuts import render, redirect, reverse
from django.views import View


def save_repository_name_in_session(request):
    repository_key = 'repository'
    repository_value = request.POST[repository_key]
    request.session[repository_key] = repository_value


def get_organization_repository_from_session(request):
    return request.session['repository'].split('/')


class searchRepository(View):
    def post(self, request):
        save_repository_name_in_session(request)
        organization, repository = get_organization_repository_from_session(request)
        kwargs = {'organization': organization,
                  'repository': repository}

        url = reverse('get_repo_info', kwargs=kwargs)
        return redirect(url)

    def get(self, request):
        return render(request, 'index.html')


