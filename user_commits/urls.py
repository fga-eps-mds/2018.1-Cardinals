from django.urls import path
from user_commits import views

urlpatterns = [
    path('getCommits/', views.getCommits, name='getCommits'),
    path('getResultCommits/', views.getResultCommits, name='getResultCommits')
]