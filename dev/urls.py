from django.conf.urls import url
from dev import views


urlpatterns = [
    url(r'getContributors/$', views.getContributors, name='getContributors')
]
