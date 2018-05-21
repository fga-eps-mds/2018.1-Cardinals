from django.urls import path
from searchDocs import views

urlpatterns = [
    path('getFiles/', views.renderingDocs, name='renderingDocs'),
]
