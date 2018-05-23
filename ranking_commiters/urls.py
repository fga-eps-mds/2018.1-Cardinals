from django.conf.urls import url
from ranking_commiters import views

urlpatterns = [
    url(r'getResult/$', views.getResult, name='getResult'),
]
