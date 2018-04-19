from django.conf.urls import url, include
from readme_doc import views

urlpatterns = [
    url(r'^', views.getReadme, name='Readme'),
]