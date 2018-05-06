from django.conf.urls import url
from ranking_commiters import views

urlpatterns = [
    url(r'getRankingCommiters/$',
        views.getRankingCommiters,
        name='getRankingCommiters'),
]
