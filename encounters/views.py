from rest_framework import viewsets

from rest_framework.authentication import BasicAuthentication 
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated 

from .models import Appointment, Encounter
from .serializers import AppointmentSerializer, EncounterSerializer

# @authentication_classes([BasicAuthentication]) 
# @permission_classes([IsAuthenticated]) 
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


# @authentication_classes([BasicAuthentication]) 
# @permission_classes([IsAuthenticated]) 
class EncounterViewSet(viewsets.ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer

