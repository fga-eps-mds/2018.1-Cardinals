from django.shortcuts import render
from django.http import HttpResponse


def searchRepository(request):

    if request.method == 'POST':
        repository = request.POST['repository']
        response = HttpResponse(repository)
        return response

    return render(request, 'index.html')
