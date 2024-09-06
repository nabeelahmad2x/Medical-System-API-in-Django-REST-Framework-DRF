from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from permission_classes import permissions
from permission_classes.permissions import admin_auth_required

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Appointment, Encounter
from .serializers import AppointmentSerializer, EncounterSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


    # searchfield
    # filter function
    # implement all 5 methods of a viewset..
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['get'])
    def cancel_appointment(self, request, *args, **kwargs):
        appointment = self.get_object()
        appointment.status = 'Cancelled'
        serializer = self.get_serializer(appointment, data={'status': 'Cancelled'}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class EncounterViewSet(viewsets.ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer


# this function was made to print the data of nesting instances in encounter..
# now commented out because to_representation of EncounterSerializer is overridden to do same work..
# custom decorator of Admin Authentication was used here which is now not in use..
# @api_view(['GET'])
# @admin_auth_required
# def get_encounter_details(request, encounter_id):
#     encounter = Encounter.objects.get(pk=encounter_id)
#
#     if encounter:
#         appointment = encounter.appointment
#         doctor = appointment.doctor
#         patient = appointment.patient
#         medicine = encounter.prescription
#
#         return Response({
#             f"Encounter ID: {encounter.id},"
#             f"Notes: {encounter.notes},"
#             f"Prescription: {medicine},"
#             f"Appointment Details:"
#             f"  Appointment ID: {appointment.id},"
#             f"  Date & Time: {appointment.appointment_datetime},"
#             f"Doctor Details:"
#             f"  Doctor ID: {doctor.id},"
#             f"  Name: {doctor.name},"
#             f"  Contact: {doctor.contact},"
#             f"  Email: {doctor.email},"
#             f"  Designation: {doctor.designation},"
#             f"  Speciality: {doctor.speciality}\n"
#             f"Patient Details:"
#             f"  Patient ID: {patient.id},"
#             f"  Name: {patient.name},"
#             f"  Contact: {patient.contact},"
#             f"  Email: {patient.email},"
#             f"  Date of Birth: {patient.date_of_birth},"
#             f"  Blood Group: {patient.blood_group},"
#             f"  Disease Stage: {patient.disease_stage}."
#         })
#     else:
#         return Response({"404: Encounter not Found :D"}, status=status.HTTP_404_NOT_FOUND)


# gets called when an encounter is saved, to change appointment status from scheduled to complete.
@receiver(post_save, sender=Encounter)
def update_appointment_status(sender, instance, **kwargs):
    appointment = instance.appointment

    if appointment.status == 'Scheduled':
        appointment.status = 'Completed'
        appointment.save()
        return Response({f'Appointment {appointment.id} status updated to: {appointment.status}'},
                        status=status.HTTP_200_OK)
    return Response({'error': 'Appointment is not scheduled or already completed.'},
                    status=status.HTTP_400_BAD_REQUEST)
