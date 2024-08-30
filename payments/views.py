from rest_framework import viewsets

from .models import PaymentHistory
from .serializers import PaymentHistorySerializer



class PaymentHistoryViewSet(viewsets.ModelViewSet):
    queryset = PaymentHistory.objects.all()
    serializer_class = PaymentHistorySerializer
