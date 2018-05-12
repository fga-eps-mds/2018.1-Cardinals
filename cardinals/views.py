from django.shortcuts import render


def index(request):

    if request.method == 'POST':
        repository = request.POST['repository']

        return repository

    return render(request, 'index.html')
