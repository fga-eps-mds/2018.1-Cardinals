from django.shortcuts import render

def getRepository(request):
    repository = request.POST['repository']

    return repository

def index(request):
    return render(request, 'index.html')