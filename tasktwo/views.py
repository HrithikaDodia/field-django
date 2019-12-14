from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from .models import *
from .serializers import FieldEncryptSerializer
# Create your views here.
class FieldEncryptUpdateView(UpdateAPIView):
  queryset = FieldEncrypt.objects.all()
  serializer_class = FieldEncryptSerializer
