from django.shortcuts import render


def getReposytory(request):
    repository = request.POST['repository']

    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')