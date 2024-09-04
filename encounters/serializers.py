from rest_framework import serializers

from .models import Appointment, Encounter
from users.models import Doctor, Patient


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = Appointment
        fields = '__all__'

    def validate(self, data):  # validation of custom appointment datetime that only future can be booked
        pass

    def create(self, validated_data):  # validation that creates with default=scheduled
        pass

    def update(self, instance, validated_data):  # update any entity
        pass

    def to_representation(self, instance):  # return objects of doctor and patient also..
        pass


class EncounterSerializer(serializers.ModelSerializer):
    appointment = serializers.PrimaryKeyRelatedField(queryset=Appointment.objects.all())

    class Meta:
        model = Encounter
        fields = '__all__'
