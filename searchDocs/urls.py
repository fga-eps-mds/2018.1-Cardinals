from django.conf.urls import url
from searchDocs import views

urlpatterns = [
    url(r'getContributingFile/$', views.getContributingFile, name='getContributingFile'),
<<<<<<< HEAD
    url(r'getLicenseFile/$', views.getLicenseFile, name='getLicenseFile'),
]

=======
]
>>>>>>> 5e37c87c42a1065b68f8e5f70df898ba9af76d6a
