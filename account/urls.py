from django.contrib import admin
from django.urls import path, include
from .import views
from .views import project_list
from account.views import (
    sing_in, sing_up, dashboard, log_out,
    forgot_password, update_password,invest ,update_profil , index
)
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login', sing_in, name='sing_in'),
    path('register', sing_up, name='sing_up'),
    path('Déconnecter', log_out, name='log_out'),
    path('ajout', invest, name='invest'),
    path('profile', update_profil, name='update_profil'),
    path('forgot-password', forgot_password, name='forgot_password'),
    path('update-password', update_password, name='update_password'),
    path('add_project/', views.add_project, name='add_project'),
    path('index', index, name ='index'),
    path('projects/', project_list, name='project_list'),
]
