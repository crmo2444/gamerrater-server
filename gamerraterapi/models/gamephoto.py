from django.db import models

class GamePhoto(models.Model):

    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    photo = models.CharField(max_length=250)