"""
Here you have to register the diferents models of your app
"""

from django.contrib import admin
from .models import Continent, Country


admin.site.register([Country, Continent])
