from django.db import models

# Create your models here.
class Eleve(models.Model):
    nom_eleve = models.TextField(max_length=50,blank=True)
    prenom_eleve = models.TextField(max_length=50,blank=True)
    nom_parents_1 = models.TextField(max_length=50,blank=True)
    prenom_parents_1 = models.TextField(max_length=50,blank=True)
    telephone_parents_1 = models.TextField(max_length=50,blank=True)
    courriel_parents_1 = models.TextField(max_length=75,blank=True)
    nom_parents_2 = models.TextField(max_length=50,blank=True)
    prenom_parents_2 = models.TextField(max_length=50,blank=True)
    telephone_parents_2 = models.TextField(max_length=50,blank=True)
    courriel_parents_2 = models.TextField(max_length=75,blank=True)
    photo = models.TextField(max_length=150,blank=True)
    non_enseignant = models.BooleanField(default=True)

    def __str__(self):
        return self.prenom_eleve + " " + self.nom_eleve
