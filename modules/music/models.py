from django.db import models
from modules.authors.models import Author

# Create your models here.
GENEROS = (
    ("RC", "Rock"),
    ("PP", "Pop"),
    ("CL", "Club"),
    ("RG", "Reggaetón"),
    ("BD", "Banda"),
    ("EL", "Electrónica"),
    ("OT", "Otro"),
)

class Album(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    anio = models.IntegerField()
    rating = models.DecimalField(max_digits = 3, decimal_places=2, default=0.00, blank=True,null=True)
    autor = models.ForeignKey(Author,
        on_delete = models.CASCADE, null=True, blank=True)
    genero = models.CharField(choices = GENEROS, max_length = 20)


class Cancion(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    anio = models.IntegerField()
    rating = models.DecimalField(max_digits = 3, decimal_places=2, default=0.00, blank=True,null=True)
    album = models.ForeignKey(Album, on_delete = models.CASCADE, related_name = "albums")
    genero = models.CharField(choices = GENEROS, max_length = 20)