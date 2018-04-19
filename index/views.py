from django.shortcuts import render


def searchRepository(request):

    if request.method == 'POST':
        repository = request.POST['repository']

        return repository

    return render(request, 'index.html')
