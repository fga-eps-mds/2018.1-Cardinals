from django.urls import path
from ranking_commiters import views

urlpatterns = [
    path('getResult/<int:repo_id>/', views.getResult, name='getResult'),
]
