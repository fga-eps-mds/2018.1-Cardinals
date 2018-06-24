from django.conf.urls import include
from django.urls import path
from cardinals import views
from django.contrib.auth import views as auth_views

import login_github.views as login_views


urlpatterns = [
    path('', views.searchRepository.as_view(), name='index'),
    path('pyGithub/', include('pygithub_api_integration.urls')),
    path('<str:organization>/<str:repository>/', include('redirecter.urls')),
    path('<str:organization>/<str:repository>/', include('time_issue.urls')),
]

urlpatterns += [
    path('home/', login_views.home, name='home'),
    path('<str:login>/', login_views.organization, name='organization'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),  # <--
]