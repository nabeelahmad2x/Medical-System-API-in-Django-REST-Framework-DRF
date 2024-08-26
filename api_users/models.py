from django.db import models
from django.contrib.auth.models import AbstractBaseUser

import bcrypt


# Person model inheriting AbstractBaseUser..
class CustomUser(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=40)
    contact = models.CharField(unique=True, max_length=20)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'contact', 'date_of_birth']

    class Meta:
        abstract = True

    


# Doctor model inherits from CustomUser..
class Doctor(CustomUser):
    designation = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    is_staff = True
    is_superuser = False

    def __str__(self):
        return f"Doctor(ID: {self.id}, Name: {self.name}, Contact: {self.contact}, Email: {self.email}, Date of Birth: {self.date_of_birth}, Designation: {self.designation}, Speciality: {self.speciality}, Active Status: {self.is_active})"


# Patient model inherits from CustomUser..
class Patient(CustomUser):
    blood_group = models.CharField(max_length=3)
    disease_stage = models.CharField(max_length=255)

    def __str__(self):
        return f"Patient(ID: {self.id}, Name: {self.name}, Contact: {self.contact}, Email: {self.email}, Date of Birth: {self.date_of_birth}, Blood Group: {self.blood_group}, Disease Stage: {self.disease_stage})"