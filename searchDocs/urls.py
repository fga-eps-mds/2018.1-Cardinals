from django.conf.urls import url
from searchDocs import views

urlpatterns = [
    url(r'getFiles/$', views.renderingDocs, name='renderingDocs'),
]
