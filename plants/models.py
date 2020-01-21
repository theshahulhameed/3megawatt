import uuid
import logging
import requests

from django.db import models
from django.conf import settings

logger = logging.getLogger(__name__)

class Plant(models.Model):
    uid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def pull_and_update_readings(self, from_date, to_date):
        '''
        Fetches the latest data for the particular time-range 
        from the monitoring service and update the corresponding
        data points.
        '''
        monitoring_service_url = settings.MONITORING_SERVICE_URL
        query_string = f"{monitoring_service_url}?plant-id={self.pk}&from={from_date}&to={to_date}"
        try:
            response = requests.request(method="GET",
                                        url=query_string,
                                        timeout=10)
        except requests.exceptions.Timeout as e:
            logger.warning("Timeout error while communicating with"
                           "monitoring service {}".format(e))
        response = requests.get(query_string)
        plant_data = response.json()
        for data in plant_data:
            plant_data_object = PlantData.objects.update_or_create(
                plant=self,
                reading_time=data['datetime'],
                defaults={
                    'energy_observed': data['observed']['energy'],
                    'energy_expected': data['expected']['energy'],
                    'irradiation_observed': data['observed']['irradiation'],
                    'irradiation_expected': data['expected']['irradiation']
                }
            )
        logger.info(
            "Fetched the data from monitoring service and updated the data")
        return True


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