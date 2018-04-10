from django.shortcuts import render
from django.http import HttpResponse

def develops(request):
    return render(request, 'develops.html')

def home_page(request):
    return render(request, 'home_page.html')
