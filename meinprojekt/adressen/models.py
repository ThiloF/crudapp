from tabnanny import verbose
from django.urls import reverse
from django.db import models

# Create your models here.

class Adressen(models.Model):
    vorname = models.CharField(max_length=50)
    nachname = models.CharField(max_length=50)
    strasse = models.CharField(max_length=50)
    plz = models.IntegerField()
    ort = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.nachname 

    def get_absolute_url(self):
        return reverse("adress_detail", args=[str(self.id)])

    class Meta:
        verbose_name = "Adressen"
        verbose_name_plural = "Adressen"
    