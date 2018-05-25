from django.urls import path
from time_issue import views

urlpatterns = [
    path('', views.timeIssue, name='timeIssue'),
]
