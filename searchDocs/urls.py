from django.urls import path
from searchDocs import views

urlpatterns = [
    path('getFiles/<int:repo_id>/', views.renderingDocs, name='renderingDocs'),
]
