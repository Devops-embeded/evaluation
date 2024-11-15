from django import forms
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


class SkillForm:
    pass


class AvailabilityForm:
    pass


class User:
    pass



class ExchangeForm(forms.ModelForm):
    # Ajoutez un champ pour sélectionner un utilisateur parmi ceux qui sont enregistrés
    provider = forms.ModelChoiceField(queryset=User.objects.all(), label="Sélectionner un prestataire")
    skill = forms.ModelChoiceField(queryset=Skill.objects.all(), label="Sélectionner une compétence")
    date = forms.DateField(widget=forms.SelectDateWidget(), label="Date de l'échange")

    class Meta:
        model = Exchange
        fields = ['provider', 'skill', 'date']