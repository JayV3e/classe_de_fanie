from django.db import models

# Create your models here.
class Eleve(models.Model):
    nom_eleve = models.TextField(max_length=50)
    prenom_eleve = models.TextField(max_length=50)
    nom_parents_1 = models.TextField(max_length=50)
    prenom_parents_1 = models.TextField(max_length=50)
    telephone_parents_1 = models.TextField(max_length=50)
    courriel_parents_1 = models.TextField(max_length=75)
    nom_parents_2 = models.TextField(max_length=50)
    prenom_parents_2 = models.TextField(max_length=50)
    telephone_parents_2 = models.TextField(max_length=50)
    courriel_parents_2 = models.TextField(max_length=75)
    photo = models.TextField(max_length=150)

    def __str__(self):
        return self.prenom_eleve + " " + self.nom_eleve
