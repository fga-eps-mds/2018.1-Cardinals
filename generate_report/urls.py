from django.urls import path
from generate_report import views

urlpatterns = [
    path('pdf_view/<int:repo_id>/', views.pdf_view, name='pdf_view'),
]
