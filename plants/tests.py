import json
from decimal import *

from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Plant, DataPoint
from api.serializers import PlantSerializer

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



'''
Tests for GET, POST, PUT and DELETE for Plant
'''


class GetAllPlantsTest(APITestCase):
    """
    Test fetching list of plants
    """

    def setUp(self):
        Plant.objects.create(name='test1')
        Plant.objects.create(name='test2')

    def test_get_all_plants(self):
        # Get API response
        response = self.client.get(reverse('get-post-plants'))
        # Get data from DB
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetIndividualPlantTest(APITestCase):
    """
    Test fetching a valid and invalid single plant
    """

    def setUp(self):
        self.plant_a = Plant.objects.create(
            name='plantA')
        self.plant_b = Plant.objects.create(
            name='plantB')

    def test_get_valid_single_plant(self):
        response = self.client.get(
            reverse('get-delete-update-plant', kwargs={'pk': self.plant_a.pk}))
        plant = Plant.objects.get(pk=self.plant_a.pk)
        serializer = PlantSerializer(plant)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_plant(self):
        response = self.client.get(
            reverse('get-delete-update-plant', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewPlantTest(TestCase):
    """ Test module for inserting a new plant """

    def setUp(self):
        self.valid_payload = {
            'name': 'PlantA',
        }
        self.invalid_payload = {
            'name': '',
        }

    def test_create_valid_plant(self):
        response = self.client.post(
            reverse('get-post-plants'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_plant(self):
        response = self.client.post(
            reverse('get-post-plants'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSinglePlantTest(TestCase):
    """ Test module for updating an existing plant record """

    def setUp(self):
        self.plant_a = Plant.objects.create(
            name='PlantA')
        self.plant_b = Plant.objects.create(
            name='PlantB')
        self.valid_payload = {
            'name': 'PlantC',
        }
        self.invalid_payload = {
            'name': '',
        }

    def test_valid_update_plant(self):
        response = self.client.put(
            reverse('get-delete-update-plant', kwargs={'pk': self.plant_a.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_plant(self):
        response = self.client.put(
            reverse('get-delete-update-plant', kwargs={'pk': self.plant_a.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSinglePlantTest(TestCase):
    """ Test module for deleting an existing plant record """

    def setUp(self):
        self.plant_a = Plant.objects.create(
            name='plantA')
        self.plant_b = Plant.objects.create(
            name='plantB')

    def test_valid_delete_plant(self):
        response = self.client.delete(
            reverse('get-delete-update-plant', kwargs={'pk': self.plant_a.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_plant(self):
        response = self.client.delete(
            reverse('get-delete-update-plant', kwargs={'pk': '30'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
