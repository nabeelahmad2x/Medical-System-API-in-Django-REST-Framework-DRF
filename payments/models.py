from django.db import models

from encounters.models import Encounter

class PaymentHistory(models.Model):
    id = models.AutoField(primary_key=True)
    encounter = models.OneToOneField(Encounter, on_delete=models.CASCADE)
    total_fee = models.FloatField()
    payment_status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Payment ID: {self.id}, Encounter: {self.encounter}, Total Fee: {self.total_fee}, Payment Status: {self.payment_status}"
