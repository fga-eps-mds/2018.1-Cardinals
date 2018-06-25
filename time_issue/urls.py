from django.urls import path
from time_issue import views

urlpatterns = [
    path('time_issue/', views.analyze_issue_graph, name='time_issue'),
]
