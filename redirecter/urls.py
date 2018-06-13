from django.urls import path
from commits_charts.views import analyze_commits_charts
from pull_request_metrics.views import analyze_pull_requests


urlpatterns = [
    path('commits_charts/', analyze_commits_charts, name='commits_charts'),
    path('pull_requests/', analyze_pull_requests, name='pull_requests'),
]