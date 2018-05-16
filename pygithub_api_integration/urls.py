from django.urls import path
from pygithub_api_integration import views


urlpatterns = [
    path('getContributors/', views.getContributors, name='getContributors'),
    path('getRepoInfo/', views.getRepoInfo, name='getRepoInfo')
]
