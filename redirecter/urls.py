from django.urls import path
from commits_charts.views import analyze_commits_charts
from pull_request_metrics.views import analyze_pull_requests
from pygithub_api_integration.views import get_repo_info
from searchDocs.views import rendering_docs
from ranking_commiters.views import ranking_commiters
from time_issue.views import analyze_issue_graph


urlpatterns = [
    path('', get_repo_info, name='get_repo_info'),
    path('community/', rendering_docs, name='community'),
    path('commits_charts/', analyze_commits_charts, name='commits_charts'),
    path('pull_requests/', analyze_pull_requests, name='pull_requests'),
    path('ranking_commiters/', ranking_commiters, name='ranking_commiters'),
    path('time_issue/', analyze_issue_graph, name='time_issue'),
]
