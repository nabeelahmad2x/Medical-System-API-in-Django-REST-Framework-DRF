from django.db import models

from api_users.models import Patient

# Create your models here.
class MedicalHistory(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    medications = models.TextField() # used teextfield instead of charfield because size of text can be large..
    surgeries = models.TextField()
    allergies = models.TextField()
    health_conditions = models.TextField()

    def __str__(self):
        return f"Medical History ID: {self.id}, Patient: {self.patient}, Medications: {self.medications}, Surgeries: {self.surgeries}, Allergies: {self.allergies}, Health Conditions: {self.health_conditions}"
