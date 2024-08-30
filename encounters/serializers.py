from rest_framework import serializers

from .models import Appointment, Encounter
from users.models import Doctor, Patient

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    
    class Meta:
        model = Appointment
        fields = '__all__'


class EncounterSerializer(serializers.ModelSerializer):
    appointment = serializers.PrimaryKeyRelatedField(queryset=Appointment.objects.all())

    class Meta:
        model = Encounter
        fields = '__all__'
