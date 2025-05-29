from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100, unique=True)
    temperature = models.FloatField()
    condition = models.CharField(max_length=100)
    humidity = models.FloatField()
    wind_speed = models.FloatField()

    def __str__(self):
        return self.city
