# records/views.py
from rest_framework import viewsets
from .models import Prescription
from .serializers import PrescriptionSerializer
from django.shortcuts import render

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all().order_by('-uploaded_at')
    serializer_class = PrescriptionSerializer


def index(request):
    return render(request, 'homepage.html')


def patient_records(request):
    return render(request, 'record2.html')
