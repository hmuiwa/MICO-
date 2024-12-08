from django.db import models

# Create your models here.

class Appointment(models.Model):
    patient_name = models.CharField(max_length=200)
    doctors_name = models.CharField(max_length=200)
    department_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    symptoms= models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.patient_name


class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name


class member(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name