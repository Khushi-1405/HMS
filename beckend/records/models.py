# records/models.py
from django.db import models

class Prescription(models.Model):
    image = models.ImageField(upload_to='prescriptions/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
