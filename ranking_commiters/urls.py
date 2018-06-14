from django.urls import path
from ranking_commiters import views

urlpatterns = [
    path('getResult/', views.getResult, name='getResult'),
]
