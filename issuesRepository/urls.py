from django.urls import path
from issuesRepository import views

urlpatterns = [

    path('getIssues/', views.getIssues, name='getIssues'),
    path('getResults/', views.getResultIssues, name='getResultIssues'),

]