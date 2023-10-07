from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DriverSerializer
from .models import Driver
from rest_framework.response import Response
from django.db.models import Min
from rest_framework.decorators import action

class DriverViewSet(viewsets.ModelViewSet):
  # queryset = Driver.objects.all()
  serializer_class = DriverSerializer

  # 'DriverViewSet' should either include a `queryset` attribute, 
  # or override the `get_queryset()` method.
  def get_queryset(self):
    drivers = Driver.objects.all()
    return drivers