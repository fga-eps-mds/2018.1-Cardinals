from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def searchRepository(request):
    if request.method == 'POST':
        repository = request.POST['repository']

        return repository
    else:
        message = 'Repositório não encontrado!'
        return message
