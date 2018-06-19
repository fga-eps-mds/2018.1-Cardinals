import os

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.decorators import action

from api.models import Repository
from api.serializers import *
from django.http import JsonResponse
import json

from api.address_handler import get_repository

class RepositoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Repository view set, ReadOnlyModelViewSet
    """
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    lookup_field = 'full_name'

    def retrieve(self, request, full_name='null'):

        repo = self.get_object()

        custom_data = {
            'Repository': RepositorySerializer(repo).data
        }

        contrib = Contributor.objects.filter(repository__full_name__contains=repo.full_name) 

        custom_data.update({
            'Contributors': ContributorSerializer(contrib, many=True).data
        })

        return Response(custom_data)


# http://localhost:8000/request/?address=https://github.com/HaskellTeam/TheGame
def api_request(request):
    address = request.GET["address"]
    repo = get_repository(address)
    status = repo != None

    if status == True:
        return JsonResponse({'status':status, 'name':repo.name, 'dbId':repo.id})
    else:
        return JsonResponse({'status':status})
