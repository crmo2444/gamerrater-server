"""View module for handling requests about category types"""
from unicodedata import category
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gamerraterapi.models import GameCategories
from gamerraterapi.models.category import Category
from gamerraterapi.models.game import Game

class GameCategoryView(ViewSet):
    """Level up category types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single category type

        Returns:
            Response -- JSON serialized category type
        """
        try:
            game_category = GameCategories.objects.get(pk=pk)
            serializer = GameCategorySerializer(game_category)
            return Response(serializer.data)
        except GameCategories.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all category types

        Returns:
            Response -- JSON serialized list of category types
        """
        game_categories = GameCategories.objects.all()

        serializer = GameCategorySerializer(game_categories, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        category = Category.objects.get(pk=request.data["category"])
        game = Game.objects.get(pk=request.data["game"])

        game_category = GameCategories.objects.create(
            category=category,
            game=game,
        )
        serializer = GameCategorySerializer(game_category)
        return Response(serializer.data)

    def destroy(self, request, pk):
        game_category = GameCategories.objects.get(pk=pk)
        game_category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GameCategorySerializer(serializers.ModelSerializer):
    """JSON serializer for category types
    """
    class Meta:
        model = GameCategories
        fields = ('id', 'category', 'game')