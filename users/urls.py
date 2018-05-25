from django.conf.urls import url, include
from users import views

urlpatterns = [
    url(r'^$', views.showInfos, name='user'),
]