from rest_framework import serializers
from .models import SvgFile

class SvgFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SvgFile
        fields = ('id', 'name')