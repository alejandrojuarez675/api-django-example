from django.contrib import admin
from .models import Continent, Country

# Register your models here.
admin.site.register(Country)
admin.site.register(Continent)