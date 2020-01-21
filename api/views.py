from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from plants.models import Plant, generate_plant_data_reports
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


class PlantDataReportsAPI(APIView):
    '''
    This will be a GET based API, which will have the
    plant uid as 'pk', 'month' and 'year' as URL parameters,
    'type' as an optional parameter to filter the results to
    the type of reading as either energy/irradiation or both.
    API generates the monthly report with an aggregated value
    of the data points per day. 
    '''

    def get(self, request, pk):
        try:   
            plant_id = pk
            month = int(request.GET.get('month'))
            year = int(request.GET.get('year'))
            reading_type = request.GET.get('type')
            plant_object = Plant.objects.get(uid=plant_id)
            response = generate_plant_data_reports(
                month=month,
                year=year,
                plant_object=plant_object,
                reading_type=reading_type)
            return Response(response, status=status.HTTP_200_OK)
        except TypeError:
            data_has_error = "Invalid query parameters."
            return Response(data_has_error, status=status.HTTP_400_BAD_REQUEST)