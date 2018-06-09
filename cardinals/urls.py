from django.conf.urls import include
from django.urls import path
from cardinals import views

urlpatterns = [
    path('', views.searchRepository, name='index'),
    path('pyGithub/', include('pygithub_api_integration.urls')),
    path('searchDocs/', include('searchDocs.urls')),
    path('rankingCommiters/', include('ranking_commiters.urls')),
    path('users/', include('users.urls')),
    path('issues/', include('time_issue.urls')),
    path('<str:organization>/<str:repository>/', include('pull_request_metrics.urls')),
]
