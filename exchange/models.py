from django.contrib.auth.models import User
from django.db import models

# Modèle pour l'activité
class Activity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255, default='Default Location')  # Valeur par défaut

    def __str__(self):
        return self.title


class Skill(models.Model):
    id = models.AutoField(primary_key=True)  # Ajoutez explicitement l'ID si nécessaire
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    level = models.IntegerField()
    def __str__(self):
        return self.name

# Modèle pour la disponibilité
class Availability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilisateur lié
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)  # Compétence liée
    day = models.DateField()  # Date de disponibilité
    time = models.TimeField()  # Exemple de champ time

    def __str__(self):
        return f"{self.user.username} - {self.skill.name} on {self.date}"

# Modèle pour l'échange de compétences
class Exchange(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requested_exchanges")  # Demandeur
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="provided_exchanges")  # Fournisseur de la compétence
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)  # Compétence concernée
    level = models.IntegerField()

    date = models.DateField()  # Date de l'échange

    def __str__(self):
        return f"{self.requester.username} booked with {self.provider.username} for {self.skill.name} on {self.date}"
