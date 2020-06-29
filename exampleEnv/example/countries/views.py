from django.shortcuts import render
from rest_framework import viewsets
from .models import Continent, Country
from .serializers import ContinentSerializer, CountrySerializer

class ContinentViewSet(viewsets.ModelViewSet):
    serializer_class = ContinentSerializer
    queryset = Continent.objects.all()

class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
