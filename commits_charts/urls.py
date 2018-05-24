from django.conf.urls import url
from commits_charts import views


urlpatterns = [
    url(r'commits_charts/$', views.commits_charts, name='commits_charts')
]
