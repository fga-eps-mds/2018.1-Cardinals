from django.shortcuts import render

def home(request):
    print('Hi, im home')
    return render(request, 'home_login.html')