from rest_framework import serializers
from regions import models

class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Regions
        fields = '__all__'