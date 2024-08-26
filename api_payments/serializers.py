from rest_framework import serializers
from .models import Encounter, PaymentHistory


class PaymentHistorySerializer(serializers.ModelSerializer):
    encounter = serializers.PrimaryKeyRelatedField(queryset=Encounter.objects.all())

    class Meta:
        model = PaymentHistory
        fields = '__all__'
