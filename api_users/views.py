from rest_framework import viewsets

from .models import Doctor, Patient
from .serializers import DoctorSerializer, PatientSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    # {    
    # "email": "aql11@email.com",
    # "name": "aqlahmd123",    
    # "contact": "03111234567",
    # "date_of_birth": "1999-11-11",
    # "password": "aql123123",
    # "designation":"doctor",
    # "speciality":"opd"
    # }

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    
# {    
#     "email": "zayamlk@email.com",
#     "name": "zayamalik",    
#     "contact": "03222124444",
#     "date_of_birth": "1990-02-12",
#     "password": "zayaamlik123",
#     "blood_group":"AB+",
#     "disease_stage":"0"
# }