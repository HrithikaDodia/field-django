from .models import *
from rest_framework import serializers

class FieldEncryptSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldEncrypt
        fields = ['file_up']
