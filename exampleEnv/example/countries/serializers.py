from .models import Country, Continent
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = '__all__'