from rest_framework import serializers
from basic_api.models import apiModel

class apiSerializer(serializers.ModelSerializer):
    class meta:
        model=apiModel
        fields=['name','desc']
