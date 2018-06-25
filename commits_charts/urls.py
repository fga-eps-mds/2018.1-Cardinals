from django.urls import path
from commits_charts import views

urlpatterns = [
    path('commits_charts/',
         views.analyze_commits_charts,
         name='commits_charts'),
]
