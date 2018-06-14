from django.urls import path
from commits_charts.views import analyze_commits_charts
from pull_request_metrics.views import analyze_pull_requests
from pygithub_api_integration.views import getRepoInfo
from searchDocs.views import renderingDocs


urlpatterns = [
    path('', getRepoInfo, name='get_repo_info'),
    path('community/', renderingDocs, name='community'),
    path('commits_charts/', analyze_commits_charts, name='commits_charts'),
    path('pull_requests/', analyze_pull_requests, name='pull_requests'),
]