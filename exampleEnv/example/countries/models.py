"""
Models file

In this files you have to put the models of the app
"""

from django.db import models

class Continent(models.Model):
    """
    Continent Model
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Country(models.Model):
    """
    Country Model
    """
    name = models.CharField(max_length=100)
    population = models.IntegerField(blank=True, null=True)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
