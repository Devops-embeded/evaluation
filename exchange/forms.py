from django import forms
from django.contrib.auth.models import User  # Importer le modèle User de Django
from .models import Skill, Availability, Activity, Exchange

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['title', 'description', 'location']  # Inclure 'location' dans le formulaire

    # Vous pouvez ajouter des validations supplémentaires si nécessaire
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Ce champ est obligatoire.")
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise forms.ValidationError("Ce champ est obligatoire.")
        return description

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'level']  # Exemple de champs, à adapter selon votre modèle

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['day', 'time']  # Exemple de champs, à adapter selon votre modèle


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='Prénom', required=False, max_length=30)
    last_name = forms.CharField(label='Nom', required=False, max_length=30)
    email = forms.EmailField(label='Adresse email', required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ExchangeForm(forms.ModelForm):
    class Meta:
        model = Exchange
        fields = ['provider', 'skill', 'date']  # Champs disponibles dans le formulaire
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }