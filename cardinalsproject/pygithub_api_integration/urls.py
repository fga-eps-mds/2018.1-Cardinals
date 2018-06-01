from django.urls import path
from pygithub_api_integration import views

urlpatterns = [
    path('getRepoInfo/', views.getRepoInfo, name='getRepoInfo')
]
