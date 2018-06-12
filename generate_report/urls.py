from django.urls import path
from generate_report import views

urlpatterns = [
    path('pdfView/', views.pdfView, name='pdfView'),
]
