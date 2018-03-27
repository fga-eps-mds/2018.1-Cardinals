from django.conf.urls import url, include
from django.contrib import admin
from dev import views

urlpatterns = [
    url(r'^', views.develops, name='Develops')
]
