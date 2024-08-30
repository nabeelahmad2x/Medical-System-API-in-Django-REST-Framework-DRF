from rest_framework import viewsets


from .models import MedicalHistory
from .serializers import MedicalHistorySerializer

# Create your views here.
class MedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
