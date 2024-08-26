from django.db import models



class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    purpose = models.TextField()
    formula = models.TextField(unique=True)

    def __str__(self):
        return f"Medcine ID: {self.id}, Medicine Name: {self.name}, Purpose: {self.purpose}, Formula: {self.formula}"