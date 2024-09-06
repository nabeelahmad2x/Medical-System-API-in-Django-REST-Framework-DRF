from datetime import datetime
import pytz
from rest_framework import serializers

from .models import Appointment, Encounter
from users.models import Doctor, Patient
from users.serializers import DoctorSerializer, PatientSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = Appointment
        fields = '__all__'

    def validate(self, data):
        if self.partial is False:
            appointment_datetime = data.get("appointment_datetime")

            if appointment_datetime < datetime.now().astimezone(pytz.utc):
                raise serializers.ValidationError(detail='The appointment datetime must be in the future')
        return data

    def create(self, data):  # creates with default=Scheduled
        appointment = Appointment.objects.create(**data)

        # set status to scheduled on creation
        appointment.status = 'Scheduled'
        appointment.save()
        return appointment

    def update(self, instance, data):  # update status to cancel on request from view_set
        # check if received data is sent to cancel then update status to 'cancelled'
        if data.get('status') == 'Cancelled':
            instance.status = 'Cancelled'
            instance.save()
            return instance

    def to_representation(self, instance):  # return objects of doctor and patient also...
        representation = super().to_representation(instance)
        representation['doctor'] = DoctorSerializer(instance.doctor).data
        representation['patient'] = PatientSerializer(instance.patient).data
        return representation


class EncounterSerializer(serializers.ModelSerializer):
    appointment = serializers.PrimaryKeyRelatedField(queryset=Appointment.objects.all())

    class Meta:
        model = Encounter
        fields = '__all__'

    def to_representation(self, instance):  # return objects of doctor and patient also...
        representation = super().to_representation(instance)
        representation['appointment'] = AppointmentSerializer(instance.appointment).data
        return representation
