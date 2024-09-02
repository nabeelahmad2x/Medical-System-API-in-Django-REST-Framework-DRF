from django.db import models

from users.models import Doctor, Patient
from medicine.models import Medicine


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_datetime = models.DateTimeField(blank=False)
    # appointment_time = models.TimeField(blank=False)
    status = models.CharField(max_length=20, default='Scheduled')

    def __str__(self):
        return f"Appointment ID: {self.id}, Doctor: {self.doctor}, Patient: {self.patient}, Date & Time: {self.appointment_datetime}, Status: {self.status}"


class Encounter(models.Model):
    id = models.AutoField(primary_key=True)
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    # encounter_datetime = durationfield??
    notes = models.TextField()
    prescription = models.ForeignKey(Medicine, on_delete=models.CASCADE, default="0")

    def __str__(self):
        return f"Encounter ID: {self.id}, Appointment: {self.appointment}, Notes: {self.notes}, Prescription: {self.prescription}"
