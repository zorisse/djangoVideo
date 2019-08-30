from django.db import models
from django.utils import timezone

# Create your models here.


class Genre (models.Model):
    #nom = models.typefield
    name = models.CharField(max_length=255)


class Movie (models.Model):
    # name = models.type de champ
    name = models.CharField(max_length=255)
    date_sortie = models.IntegerField()
    nbr_en_stock = models.IntegerField()
    prix = models.FloatField()
    # relation
    # nom = models.ForeignKey(CLass, on_delete= models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    # time stamp
    date_created = models.DateTimeField(default=timezone.now)
