from django.db import models

# Create your models here.
class Propriete(models.Model):
    NNI = models.CharField(primary_key=True, max_length=8)
    Prenom = models.CharField(max_length=50)
    Nom = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)


    def __str__(self):
        return self.Prenom


class Voiture(models.Model):
    plaque = models.CharField(max_length=16,unique=True)
    propriete = models.ForeignKey(Propriete,on_delete=models.CASCADE,null=True)
    marque = models.CharField(max_length=15)
    genre = models.CharField(max_length=15)
    couleur = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.marque



class AutoMobile(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    annee_fabrication = models.IntegerField()
    couleur = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/', null=True, blank=True)

    def __str__(self):
        return f"{self.marque} {self.modele}"