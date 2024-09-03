from rest_framework import status, viewsets
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Doctor, Patient
from .serializers import DoctorSerializer, PatientSerializer
from permission_classes.permissions import IsDoctor, IsPatient, IsAdmin


class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsDoctor | IsAdmin]

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsPatient | IsAdmin]

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# class Home(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)
