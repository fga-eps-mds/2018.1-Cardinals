from django.urls import path
from login_github import views

urlpatterns = [
    path('/login_github', views.loginGithub, name='login_github'),
]