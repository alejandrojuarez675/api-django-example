"""
File to put the differents ViewSets
"""

from rest_framework import viewsets
from .models import Continent, Country
from .serializers import ContinentSerializer, CountrySerializer

class ContinentViewSet(viewsets.ModelViewSet):
    """
    View set of the CRUD Continent
    """
    serializer_class = ContinentSerializer
    queryset = Continent.objects.all()

class CountryViewSet(viewsets.ModelViewSet):
    """
    View set of the CRUD Country
    """
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
