from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from plants.models import Plant
from .serializers import PlantSerializer



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


class UpdatePlantDataPointsAPI(APIView):
    '''
    REST API which takes the 'uid' of the plant in URL, 
    date-range(from,to) in the POST request, 
    and update the Data Points of the plant, 
    by taking the updated data from pinging monitoring service, 
    returns 200 if it's success, and 400 if it failed. 
    '''

    def post(self, request, pk):
        # Fetches the POST data
        data = request.data
        try:
            plant = Plant.objects.get(uid=pk)
            from_time = data.get('from')
            to_time = data.get('to')
            plant.pull_and_update_readings(
                from_date=from_time, to_date=to_time)
            return Response(status=status.HTTP_200_OK)
        except TypeError:
            data_has_error = "Invalid payload."
        except ConnectionError:
            data_has_error = "Error with the connection."
            return Response(data_has_error, status=status.HTTP_400_BAD_REQUEST)