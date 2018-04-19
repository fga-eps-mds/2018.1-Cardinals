from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def searchRepository(request):
    if request.method == 'POST':
        repository = request.POST['repository']

        return repository
    else:
        message = 'Repositorio nao encontrado!'
        return message


