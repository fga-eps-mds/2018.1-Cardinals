from django.conf.urls import url
from ranking_commiters import views

urlpatterns = [
    url(r'rankingCommiters/$',
        views.rankingCommiters,
        name='rankingCommiters'),
]
