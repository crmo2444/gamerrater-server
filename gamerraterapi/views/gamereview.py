"""View module for handling requests about category types"""
from unicodedata import category
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gamerraterapi.models.game import Game
from gamerraterapi.models.gamereview import GameReview
from gamerraterapi.models.player import Player

class GameReviewView(ViewSet):
    """Level up category types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single category type

        Returns:
            Response -- JSON serialized category type
        """
        try:
            game_review = GameReview.objects.get(pk=pk)
            serializer = GameReviewSerializer(game_review)
            return Response(serializer.data)
        except GameReview.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all category types

        Returns:
            Response -- JSON serialized list of category types
        """
        game_review = GameReview.objects.all()

        serializer = GameReviewSerializer(game_review, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        player = Player.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])

        game_review = GameReview.objects.create(
            player=player,
            game=game,
            review = request.data["review"]
        )
        serializer = GameReviewSerializer(game_review)
        return Response(serializer.data)

    def destroy(self, request, pk):
        game_review = GameReview.objects.get(pk=pk)
        game_review.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GameReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for category types
    """
    class Meta:
        model = GameReview
        fields = ('id', 'player', 'game', 'review')
        depth = 2