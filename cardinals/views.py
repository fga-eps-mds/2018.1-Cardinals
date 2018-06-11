from django.shortcuts import render


def getRepository(request):
    repository = request.POST['repository']

    return repository


def searchRepository(request):
    return render(request, 'index.html')
