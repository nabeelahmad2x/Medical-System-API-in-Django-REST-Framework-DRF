from rest_framework import serializers
from .models import Doctor, Patient
from .user_modules import set_password


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def create(self, data):
        password = data['password']
        hashed_password = set_password(password)

        doctor = Doctor(**data)
        doctor.password = hashed_password.decode()  
        doctor.save()
        return doctor
        

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, data):
        password = data['password']
        hashed_password = set_password(password)

        patient = Patient(**data)
        patient.password = hashed_password.decode()  
        patient.save()
        return patient