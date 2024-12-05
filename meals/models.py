from django.db import models

class Meal(models.Model):
    meal_name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100)
    price = models.FloatField()
    type = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
