from decimal import *
from django.test import TestCase
from .models import Plant, DataPoint

class PlantModelTest(TestCase):
    """
    Tests for the Plant Model
    object creation. 
    """

    def setUp(self):
        Plant.objects.create(name='test')

    def test_plant_object_created(self):
        test_object = Plant.objects.get(name='test')
        self.assertEqual(test_object.name, "test")


class DataPointTest(TestCase):
    """
    Tests for the Data Point Model
    object creation. 
    """

    def setUp(self):
        plant_object = Plant.objects.create(name='test')
        DataPoint.objects.create(
            plant=plant_object,
            energy_expected="100.0",
            energy_observed="90.0",
            irradiation_expected="100.0",
            irradiation_observed="85.0",
            reading_time="2019-01-01T00:00:00",
        )

    def test_plant_object_created(self):
        test_plant_object = Plant.objects.get(name='test')
        test_object = DataPoint.objects.get(plant=test_plant_object)
        self.assertEqual(test_object.energy_expected, Decimal("100.0"))

