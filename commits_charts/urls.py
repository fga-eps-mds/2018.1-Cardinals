from django.urls import path
from commits_charts import views


urlpatterns = [
    path('', views.commits_charts, name='commits_charts'),
]
