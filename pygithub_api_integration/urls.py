from django.conf.urls import url
from pygithub_api_integration import views

urlpatterns = [
    url(r'firstTest/', views.getPygithub, name='firstTest'),
    url(r'^getRepo/', views.getRepository, name='getRepo')
]