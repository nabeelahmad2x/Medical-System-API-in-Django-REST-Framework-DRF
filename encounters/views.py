from rest_framework import viewsets, status
from rest_framework.decorators import api_view

from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from custom_permission_classes.permissions import admin_auth_required
from .models import Appointment, Encounter
from .serializers import AppointmentSerializer, EncounterSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class EncounterViewSet(viewsets.ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer


@api_view(['GET'])
@admin_auth_required
def get_encounter_details(request, encounter_id):

    encounter = Encounter.objects.get(pk=encounter_id)

    if encounter:
        appointment = encounter.appointment
        doctor = appointment.doctor
        patient = appointment.patient
        medicine = encounter.prescription

        return Response({
            f"Encounter ID: {encounter.id},"
            f"Notes: {encounter.notes},"
            f"Prescription: {medicine},"
            f"Appointment Details:"
            f"  Appointment ID: {appointment.id},"
            f"  Date & Time: {appointment.appointment_datetime},"
            f"Doctor Details:"
            f"  Doctor ID: {doctor.id},"
            f"  Name: {doctor.name},"
            f"  Contact: {doctor.contact},"
            f"  Email: {doctor.email},"
            f"  Designation: {doctor.designation},"
            f"  Speciality: {doctor.speciality}\n"
            f"Patient Details:"
            f"  Patient ID: {patient.id},"
            f"  Name: {patient.name},"
            f"  Contact: {patient.contact},"
            f"  Email: {patient.email},"
            f"  Date of Birth: {patient.date_of_birth},"
            f"  Blood Group: {patient.blood_group},"
            f"  Disease Stage: {patient.disease_stage}."
        })
    else:
        return Response({"404: Encounter not Found :D"}, status=status.HTTP_404_NOT_FOUND)
