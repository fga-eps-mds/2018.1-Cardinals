from django.conf.urls import url
from user_commits import views

urlpatterns = [
    url(r'getCommits/$', views.getCommits, name='getCommits'),
    url(r'getResultCommits/$', views.getResultCommits, name='getResultCommits')
]
