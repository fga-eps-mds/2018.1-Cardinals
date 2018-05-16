from django.urls import path
from dev import views


urlpatterns = [
    path('getContributors/', views.getContributors, name='getContributors')
]
