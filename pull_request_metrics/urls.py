from django.urls import path
from . import views

urlpatterns = [
    path('pull_requests/', views.analyze_pull_requests, name='pull_requests'),
]