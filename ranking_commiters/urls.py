from django.conf.urls import url
from ranking_commiters import views

urlpatterns = [
    url(r'getRankingCommitersResult/$',
        views.getRankingCommitersResult,
        name='getRankingCommitersResult'),
]
