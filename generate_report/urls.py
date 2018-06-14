from django.urls import path
from generate_report import views

urlpatterns = [
    path('pdfView/<int:repo_id>/', views.pdfView, name='pdfView'),
]
