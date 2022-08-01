from unicodedata import category
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gamerraterapi.models.game import Game
from gamerraterapi.models.gamerating import GameRating
from gamerraterapi.models.player import Player

class GameRatingView(ViewSet):
    """Level up category types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single category type

        Returns:
            Response -- JSON serialized category type
        """
        try:
            game_rating = GameRating.objects.get(pk=pk)
            serializer = GameRatingSerializer(game_rating)
            return Response(serializer.data)
        except GameRating.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all category types

        Returns:
            Response -- JSON serialized list of category types
        """
        game_rating = GameRating.objects.all()

        serializer = GameRatingSerializer(game_rating, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        player = Player.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])

        game_rating = GameRating.objects.create(
            player=player,
            game=game,
            rating = request.data["rating"]
        )
        serializer = GameRatingSerializer(game_rating)
        return Response(serializer.data)

    def destroy(self, request, pk):
        game_rating = GameRating.objects.get(pk=pk)
        game_rating.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GameRatingSerializer(serializers.ModelSerializer):
    """JSON serializer for category types
    """
    class Meta:
        model = GameRating
        fields = ('id', 'player', 'game', 'rating')
        depth = 2