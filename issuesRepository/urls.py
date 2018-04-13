from django.conf.urls import url
from issuesRepository import views

urlpatterns = [
    url(r'getIssues/$', views.getIssues, name='getIssues'),
    url(r'getResults/$', views.getResultIssues, name='getResultIssues'),
]