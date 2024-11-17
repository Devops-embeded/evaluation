from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect

from .forms import SkillForm, AvailabilityForm, \
    ActivityForm, ExchangeForm, ProfileUpdateForm  # Assurez-vous d'avoir défini ces formulaires dans forms.py
from .models import Skill, Activity


# Vue pour la page d'accueil
def home(request):
    skills = Skill.objects.all()
    skills_list = [skills[i:i + 3] for i in range(0, len(skills), 3)]  # Diviser les compétences en trois colonnes
    return render(request, 'exchange/home.html', {'skills_list': skills_list})


# Vue pour le tableau de bord
@login_required
def dashboard(request):
    activities = Activity.objects.all()
    return render(request, 'exchange/dashboard.html', {'activities': activities})


# Vue pour ajouter une compétence
@login_required
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SkillForm()
    return render(request, 'exchange/add_exchange.html', {'form': form})


# Vue pour ajouter la disponibilité
@login_required
def add_availability(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AvailabilityForm()
    return render(request, 'exchange/add_availability.html', {'form': form})


# Vue pour la connexion
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'exchange/accounts/login.html', {'form': form})


# Vue pour afficher et modifier le profil
@login_required
def profile(request):
    return render(request, 'exchange/accounts/profile/profile.html')


# Vue pour changer le mot de passe
@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'exchange/accounts/password_change.html', {'form': form})


# Vue pour déconnecter l'utilisateur
def logout_view(request):
    auth_logout(request)
    return redirect('home')


# Vue pour éditer le profil de l'utilisateur
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige vers la page de profil après mise à jour
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'exchange/accounts/edit_profile.html', {'form': form})

# Vue pour ajouter une activité
@login_required
def add_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ActivityForm()
    return render(request, 'exchange/accounts/add_activity.html', {'form': form})

@login_required
def add_exchange(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirige vers le tableau de bord après déclaration
    else:
        form = ExchangeForm()

    return render(request, 'exchange/add_exchange.html', {'form': form})