from rest_framework import generics
from plants.models import Plant


class PlantsListCreateAPI(generics.ListCreateAPIView):
    '''
    REST API which handles creation of Plants
    and listing of plants
    Expects a POST request with 'name' of the plant 
    for creation.
    '''
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class PlantsDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    '''
    REST API which allows to Retrieve, Update
    and Delete individual Plants.
    Expects the 'uid' of the plant in the URL 
    '''
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
