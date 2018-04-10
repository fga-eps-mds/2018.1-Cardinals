from django.conf.urls import url
from dev import views

urlpatterns = [
    url(r'^', views.develops, name='Develops'),
    url('', views.home_page, name='home_page'),
]
