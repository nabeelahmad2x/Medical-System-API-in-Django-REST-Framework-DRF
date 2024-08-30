from rest_framework import serializers
from .models import MedicalHistory

from users.models import Patient



class MedicalHistorySerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = MedicalHistory
        fields = '__all__'
