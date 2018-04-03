from django.conf.urls import url
from pygithub_api_integration import views

urlpatterns = [
    url(r'getRepo/$', views.getRepo, name='getRepo'),
    url(r'getContributors/$', views.getContributors, name='getContributors')
]