"""
Serializers for the user API View.
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""
    
    class Meta:
        model = get_user_model()
        field = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}
    
    # vaildationに通った時に呼び出されるメソッド
    def create(self, validate_data):
        """Create and return a user with encrypted password"""
        return get_user_model().objects.create_user(**validate_data)