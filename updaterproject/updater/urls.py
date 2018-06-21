"""updater URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from api import views

urlpatterns = [
    url(r"^test", views.APIParamsTest.as_view(), name='test'),
    url(r"^repository/commits_pair_chart_data", views.RepositoryCommitVsPairData.as_view() ),
    url(r"^repository/commits", views.RepositoryCommits.as_view() ),
    url(r"^repository", views.RepositoryData.as_view() ),

]
