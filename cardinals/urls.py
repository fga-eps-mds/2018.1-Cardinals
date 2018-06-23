from django.conf.urls import include
from django.urls import path
from cardinals import views

urlpatterns = [
    path('', views.searchRepository.as_view(), name='index'),
    path('pyGithub/', include('pygithub_api_integration.urls')),
    path('<str:organization>/<str:repository>/', include('redirecter.urls')),
]
