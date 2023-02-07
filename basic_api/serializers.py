from .models import apiModel
from rest_framework import serializers

class apiSerializer(serializers.ModelSerializer):
    class Meta:
        model=apiModel
        fields=["name","des"]