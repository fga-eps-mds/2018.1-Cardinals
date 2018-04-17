from django.conf.urls import url
from user_commits import views

urlpatterns = [
    url(r'^', views.getCommits, name='Commits'),
    
]