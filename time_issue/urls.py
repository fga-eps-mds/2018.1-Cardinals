from django.urls import path
from time_issue import views

urlpatterns = [
    path('timeIssue/', views.analyze_issue_graph, name='timeIssue'),
]
