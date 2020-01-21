from rest_framework import serializers
from plants.models import Plant, DataPoint


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'


class DataPointSerializer(serializers.ModelSerializer):
    plant = PlantSerializer

    class Meta:
        model = DataPoint
        fields = '__all__'
