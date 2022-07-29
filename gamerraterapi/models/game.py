from django.db import models

class Game(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    designer = models.CharField(max_length=50)
    release_date = models.DateField()
    number_of_players = models.IntegerField()
    duration = models.TimeField()
    age_rating = models.IntegerField()