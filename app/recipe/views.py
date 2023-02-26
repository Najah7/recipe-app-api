"""
Views for recipe APIs.
"""
from rest_framework import (
    viewsets,
    mixins,    
) 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Recipe,
    Tag,
)
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs"""
    serializer_class = serializers.RecipeDetailSerializer
    # NOTE:一番汎用性の高いquerysetをここで定義(これをfilterしたりして特定のデータに対する操作を)
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    # NOTE:GET用のquerysetを定義している
    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    def get_serializer_class(self):
        """Return the serializer class for requests."""
        if self.action == 'list':
            return serializers.RecipeSerializer
        
        return self.serializer_class
    
    # NOTE:xxModeMinxinで呼び出せるメソッドの形式（ほかにもupdate、destoryなど）
    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)

class TagViewSet(mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    """Manage tags in the database."""
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Filter queryset to authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-name')