from django.db import models

class Game(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    designer = models.CharField(max_length=50)
    release_date = models.DateField()
    number_of_players = models.IntegerField()
    duration = models.IntegerField()
    age_rating = models.IntegerField()

    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = self.ratings.all()

        # Sum all of the ratings for the game
        total_rating = 0
        for rating in ratings:
            total_rating += rating.rating

        if len(ratings) != 0:
            avg = total_rating / len(ratings)
        else:
            avg = 0

        # Calculate the averge and return it.
        # If you don't know how to calculate averge, Google it.
        return avg
        #return the result