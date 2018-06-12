from django.shortcuts import render

def searchRepository(request):
    return render(request, 'index.html')
