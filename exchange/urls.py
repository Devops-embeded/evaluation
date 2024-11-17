from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name='home'),# Lien vers la vue home    #
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-skill/', views.add_skill, name='add_skill'),
    path('add-availability/', views.add_availability, name='add_availability'),
    path('accounts_login/', views.login_view, name='login'),  # Changement ici vers login_view
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/password_change/', views.password_change, name='password_change'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/edit_profile/', views.edit_profile, name='edit_profile'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/add-activity/', views.add_activity, name='add_activity'),
    path('add-exchange/', views.add_exchange, name='add_exchange'),
    path('my-exchanges/', views.my_exchanges, name='my_exchanges'),  # Ajoutez ce chemin

]
