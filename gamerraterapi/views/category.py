"""View module for handling requests about category types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gamerraterapi.models.category import Category

class CategoryView(ViewSet):
    """Level up category types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single category type

        Returns:
            Response -- JSON serialized category type
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND) 

    def list(self, request):
        """Handle GET requests to get all category types

        Returns:
            Response -- JSON serialized list of category types
        """
        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for category types
    """
    class Meta:
        model = Category
        fields = ('id', 'name')