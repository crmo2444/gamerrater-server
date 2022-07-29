from django.db import models

class GameReview(models.Model):

    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    review = models.CharField(max_length=250)