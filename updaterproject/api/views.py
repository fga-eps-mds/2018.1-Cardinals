import os

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.decorators import action

import json
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from api.models import Repository
from api.serializers import *
from django.http import JsonResponse
from github_api.update_repository import get_commits_chart_data


from api.address_handler import get_repository


class APIParamsTest(APIView):
    '''
        http://localhost:3000/test/?param=qwe%20rty
    '''

    def get(self, request, format=None):
        test_param = self.request.query_params.get('param')

        if not test_param:
            test_param = 'none param given'
        return Response({"param":test_param})

class RepositoryData(APIView):

    def getOne(self, repo_address):

        repo = get_repository(repo_address)
        status = repo != None
        custom_data = {}

        if status:
            custom_data = {
                'Repository': RepositorySerializer(repo).data
            }

            contrib = Contributor.objects.filter(repository__full_name__contains=repo.full_name) 

            custom_data.update({
                'Contributors': ContributorSerializer(contrib, many=True).data
            })
        else:
            custom_data = {"error":"could not find repository"}
        
        return custom_data

    def getAll(self):
        allRepos = Repository.objects.all()
        
        custom_data = RepositorySerializer(allRepos, many=True).data

        return custom_data

    def get(self, request, format=None):
        address = self.request.query_params.get('address')

        response_data = {}

        if address:
            response_data = self.getOne(address)
        else:
            response_data = self.getAll()
            
        return Response(response_data)


class RepositoryCommits(APIView):

    def getAll(self, repo_address):

        repo = get_repository(repo_address)
        custom_data = {}

        if repo:
            commits = Commit.objects.filter(repository__full_name__contains=repo.full_name) 

            custom_data = {
                'Repository': RepositorySerializer(repo).data,
                'Commits': CommitSerializer(commits, many=True).data
            }

        else:
            custom_data = {"error": "could not find repository"}

        return custom_data

    def get(self, request, format=None):
        address = self.request.query_params.get('address')

        response_data = {}

        if address:
            response_data = self.getAll(address)
        else:
            response_data = {"error": "address not defined"}
            
        return Response(response_data)




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


    @method_decorator(cache_page(180))
    @action(methods=['get'], detail=True)
    def commits_chart_data(self, request, full_name=None):
        dates, commits, paired = get_commits_chart_data('fga-gpp-mds/2018.1-Cardinals')

        custom_data = {
            'dates': dates,
            'commits': commits,
            'paired':paired
        }

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
