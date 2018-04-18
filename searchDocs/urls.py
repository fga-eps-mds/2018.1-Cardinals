from django.conf.urls import url
from searchDocs import views

urlpatterns = [
    url(r'getContributingFile/$', views.getContributingFile, name='getContributingFile'),
]
