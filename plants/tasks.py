import logging

from datetime import timedelta
from django.utils import timezone

from celery.task.schedules import crontab
from django.conf import settings

from threemegawatt.celery import app
from .models import Plant

logger = logging.getLogger(__name__)

@app.task
def task_update_latest_plant_data():
    """
    A periodic task which runs every day
    to fetch the latest data points from the monitoring service
    for each plant and update it. 
    """
    monitoring_service_url = settings.MONITORING_SERVICE_URL
    from_date = timezone.now().date()
    to_date = (timezone.now() + timedelta(days=1)).date()
    plants = Plant.objects.all()
    for plant in plants:
        plant.pull_and_update_readings(from_date, to_date)
    logger.info("Succesfully updated the objects")