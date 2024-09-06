from rest_framework import serializers
from .models import Doctor, Patient


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'email', 'name', 'contact', 'date_of_birth']

    def create(self, data):
        password = data['password']

        doctor = Doctor(**data)
        doctor.is_staff = True
        doctor.set_password(password)
        doctor.save()
        return doctor


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'email', 'name', 'contact', 'date_of_birth', 'blood_group', 'disease_stage']

    def create(self, data):
        password = data['password']
        patient = Patient(**data)
        patient.set_password(password)
        patient.save()
        return patient
