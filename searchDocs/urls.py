from django.conf.urls import url
from searchDocs import views

urlpatterns = [
    url(r'getContributingFile/$', views.getContributingFile, name='getContributingFile'),
    url(r'getLicenseFile/$', views.getLicenseFile, name='getLicenseFile'),
]

