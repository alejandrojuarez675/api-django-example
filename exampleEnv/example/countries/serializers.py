"""
File where you find the differents serializers of this app
"""

from rest_framework import serializers
from .models import Country, Continent

class CountrySerializer(serializers.ModelSerializer):
    """
    Serializer for CRUD of countries
    """
    class Meta:
        model = Country
        fields = '__all__'


class ContinentSerializer(serializers.ModelSerializer):
    """
    Serializer for CRUD of Continents
    """
    class Meta:
        model = Continent
        fields = '__all__'
