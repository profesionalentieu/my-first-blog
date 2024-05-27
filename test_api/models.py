from django.db import models

# Create your models here.

class Alumno(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.TextField(max_length=100, null=True)
    last_name = models.TextField(max_length=100, null=True)
    dni = models.TextField(max_length=10, null=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.first_name

class Reserva(models.Model):
    date = models.DateTimeField(null=True)
    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.date
