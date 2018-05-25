from django.shortcuts import render
from cardinals.views import getRepository


def showInfos(request):
    repository = getRepository(request)
    return render(request, 'user.html',  {"repository": repository})
