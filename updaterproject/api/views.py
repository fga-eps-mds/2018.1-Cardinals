import os

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from api.models import Repository
from api.serializers import RepositorySerializer
from django.http import JsonResponse

from api.address_handler import get_repository

class RepositoryViewSet(viewsets.ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer

# http://localhost:8000/request/?address=https://github.com/HaskellTeam/TheGame
def api_request(request):
    address = request.GET["address"]
    repo = get_repository(address)
    status = repo != None

    if status == True:
        return JsonResponse({'status':status, 'name':repo.name, 'dbId':repo.id})
    else:
        return JsonResponse({'status':status})
    




