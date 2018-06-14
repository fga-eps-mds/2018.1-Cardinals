from django.conf.urls import include
from django.urls import path
from cardinals import views

urlpatterns = [
    path('', views.searchRepository.as_view(), name='index'),
    path('pyGithub/', include('pygithub_api_integration.urls')),
    path('searchDocs/', include('searchDocs.urls')),
    path('rankingCommiters/', include('ranking_commiters.urls')),
    path('issues/', include('time_issue.urls')),
#   path('<str:organization>/<str:repository>/', include('commits_charts.urls')),
#    path('<str:organization>/<str:repository>/', include('pull_request_metrics.urls')),
    path('<str:organization>/<str:repository>/', include('redirecter.urls')),

]
