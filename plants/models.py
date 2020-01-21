import uuid
from django.db import models

class Plant(models.Model):
    uid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DataPoint(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    energy_expected = models.DecimalField(max_digits=25, decimal_places=15)
    energy_observed = models.DecimalField(max_digits=25, decimal_places=15)
    irradiation_observed = models.DecimalField(
        max_digits=25, decimal_places=15)
    irradiation_expected = models.DecimalField(
        max_digits=25, decimal_places=15)
    reading_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.plant.name}'s data on {self.reading_time}"