from rest_framework import status, viewsets
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Doctor, Patient
from .serializers import DoctorSerializer, PatientSerializer
from custom_permission_classes.permissions import IsDoctor, IsPatient


class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsDoctor]

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsPatient]

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# class Home(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)
