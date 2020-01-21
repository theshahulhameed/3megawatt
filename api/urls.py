from django.urls import path
from .views import PlantsListCreateAPI, PlantsDetailsAPI, UpdatePlantDataPointsAPI

urlpatterns = [
    path('plants/', PlantsListCreateAPI.as_view(), name='get-post-plants'),
    path('plants/<str:pk>/', PlantsDetailsAPI.as_view(), name='get-delete-update-plant'),
    path('plants/<str:pk>/update/', UpdatePlantDataPointsAPI.as_view(),
         name='update-plant-datapoints'),
]