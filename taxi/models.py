from django.db import models


class Taxi(models.Model):
    taxi_name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    pass_capacity = models.DecimalField(max_digits=10, decimal_places=2)
    car_model = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
